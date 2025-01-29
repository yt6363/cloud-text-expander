import datetime
import tkinter as tk
from tkinter import ttk, messagebox
from auth import get_user_id
from db import add_snippet, get_snippets, delete_snippet
from openai_config import load_api_key, save_api_key, delete_api_key

class SnippetManager(tk.Tk):
    def __init__(self, user_id):
        super().__init__()
        self.title("Snippet Manager")
        self.geometry("800x600")

        # Theme Setup
        self.style = ttk.Style(self)
        if "aqua" in self.style.theme_names():
            self.style.theme_use("aqua")
        else:
            self.style.theme_use("clam")

        self.user_id = user_id

        # Track snippet editing
        self.edit_mode = False        # Whether we are editing an existing snippet
        self.original_shortcut = None # The old shortcut name if renaming

        # Create the GUI sections
        self.create_header()
        self.create_theme_selector()
        self.create_snippet_form()
        self.create_snippet_list()
        self.create_ai_settings()

        # Finally, load snippets into Treeview
        self.refresh_snippets()

    def create_header(self):
        """Header with main title."""
        header_frame = ttk.Frame(self, padding=10)
        header_frame.pack(fill="x")

        ttk.Label(header_frame, text="Cloud Text Expander", font=("Helvetica", 16, "bold")).pack()
        ttk.Label(header_frame, text="Manage Your Snippets in Firebase").pack()

    def create_theme_selector(self):
        """ComboBox to switch themes."""
        theme_frame = ttk.Frame(self, padding=10)
        theme_frame.pack(fill="x")

        ttk.Label(theme_frame, text="Select Theme:").pack(side="left")
        themes = self.style.theme_names()
        self.theme_var = tk.StringVar(value=self.style.theme_use())

        theme_box = ttk.Combobox(theme_frame, textvariable=self.theme_var, values=themes, state="readonly", width=15)
        theme_box.pack(side="left", padx=5)
        theme_box.bind("<<ComboboxSelected>>", self.change_theme)

    def change_theme(self, event=None):
        """Applies new theme."""
        self.style.theme_use(self.theme_var.get())

    def create_snippet_form(self):
        """Frame for adding/editing a snippet."""
        form_frame = ttk.LabelFrame(self, text=" Add / Edit Snippet ", padding=10)
        form_frame.pack(fill="x", padx=10, pady=10)

        # Shortcut label + entry
        ttk.Label(form_frame, text="Shortcut (e.g., @@email):").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.shortcut_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.shortcut_var, width=25).grid(row=0, column=1, padx=5, pady=5)

        # Expansion label + entry
        ttk.Label(form_frame, text="Expansion:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.expansion_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.expansion_var, width=25).grid(row=1, column=1, padx=5, pady=5)

        # Save button
        self.save_button = ttk.Button(form_frame, text="Save Snippet", command=self.save_snippet)
        self.save_button.grid(row=0, column=2, rowspan=2, padx=10)

        # Status label
        self.status_label = ttk.Label(form_frame, text="", foreground="blue")
        self.status_label.grid(row=2, column=0, columnspan=3, pady=5)

    def create_snippet_list(self):
        """Treeview for existing snippets + edit/delete buttons."""
        list_frame = ttk.LabelFrame(self, text=" Existing Snippets ", padding=10)
        list_frame.pack(fill="both", expand=True, padx=10, pady=5)

        columns = ("shortcut", "expansion")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=8)
        self.tree.heading("shortcut", text="Shortcut")
        self.tree.heading("expansion", text="Expansion")
        self.tree.column("shortcut", width=120)
        self.tree.column("expansion", width=350)

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Bind selection event
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # Buttons for editing/deleting
        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill="x", padx=10, pady=5)

        ttk.Button(btn_frame, text="Edit Selected", command=self.edit_selected_snippet).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Delete Selected", command=self.delete_selected_snippet).pack(side="left", padx=5)

    def on_tree_select(self, event):
        """Called when the user selects a row in the Treeview."""
        selection = self.tree.selection()
        if not selection:
            return

        item_id = selection[0]
        snippet_data = self.tree.item(item_id, "values")
        if snippet_data:
            shortcut, expansion = snippet_data
            print(f"🔍 Selected Snippet: {shortcut} -> {expansion}")

    def edit_selected_snippet(self):
        """Loads the selected snippet into the form for editing."""
        selection = self.tree.selection()
        if not selection:
            self.status_label.config(text="No snippet selected to edit.")
            return

        item_id = selection[0]
        snippet_data = self.tree.item(item_id, "values")
        if snippet_data:
            shortcut, expansion = snippet_data
            # Fill form
            self.shortcut_var.set(shortcut)
            self.expansion_var.set(expansion)
            self.status_label.config(text=f"Editing snippet '{shortcut}'...")

    def delete_selected_snippet(self):
        """Deletes the selected snippet from Firestore."""
        selection = self.tree.selection()
        if not selection:
            self.status_label.config(text="No snippet selected to delete.")
            return

        item_id = selection[0]
        snippet_data = self.tree.item(item_id, "values")
        if snippet_data:
            shortcut, _ = snippet_data
            delete_snippet(self.user_id, shortcut)
            self.status_label.config(text=f"Deleted snippet '{shortcut}'.")
            self.refresh_snippets()

    def create_ai_settings(self):
        """Section for OpenAI API Key input & control."""
        ai_frame = ttk.LabelFrame(self, text="AI Integration", padding=10)
        ai_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(ai_frame, text="OpenAI API Key:").grid(row=0, column=0, sticky="w")
        self.api_key_var = tk.StringVar(value=load_api_key())
        self.api_entry = ttk.Entry(ai_frame, textvariable=self.api_key_var, width=40)
        self.api_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(ai_frame, text="Save Key", command=self.save_api_key).grid(row=0, column=2, padx=5)
        ttk.Button(ai_frame, text="Delete Key", command=self.delete_api_key).grid(row=0, column=3, padx=5)

    def save_api_key(self):
        """Saves OpenAI API Key."""
        api_key = self.api_key_var.get().strip()
        if api_key:
            save_api_key(api_key)
            messagebox.showinfo("Success", "✅ OpenAI API Key saved!")
        else:
            messagebox.showwarning("Error", "⚠️ Please enter a valid API key.")

    def delete_api_key(self):
        """Deletes OpenAI API Key."""
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete the API key?")
        if confirm:
            delete_api_key()
            self.api_key_var.set("")
            messagebox.showinfo("Deleted", "🗑️ OpenAI API Key deleted!")

    def refresh_snippets(self):
        """Fetch snippets from Firestore and populate the Treeview."""
        # Clear existing rows
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Load from Firestore
        all_snips = get_snippets(self.user_id)
        for shortcut, expansion in all_snips.items():
            self.tree.insert("", tk.END, values=(shortcut, expansion))

    def save_snippet(self):
        """Save or update a snippet (no distinct edit mode here)."""
        shortcut = self.shortcut_var.get().strip()
        expansion = self.expansion_var.get().strip()

        if not shortcut or not expansion:
            self.status_label.config(text="Error: Must enter both a shortcut and expansion.")
            return

        # Save/Update in Firestore
        add_snippet(self.user_id, shortcut, expansion)
        self.status_label.config(text=f"Saved snippet '{shortcut}'!")

        # Clear fields
        self.shortcut_var.set("")
        self.expansion_var.set("")
        self.refresh_snippets()

if __name__ == "__main__":
    user_id = get_user_id()
    app = SnippetManager(user_id)
    app.mainloop()
