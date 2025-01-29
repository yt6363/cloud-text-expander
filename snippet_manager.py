# snippet_manager.py
import tkinter as tk
from tkinter import ttk

class SnippetManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Snippet Manager")  # Window title
        self.geometry("400x300")       # Window size

        # Create a simple label & button just to prove it’s working
        label = ttk.Label(self, text="Hello from SnippetManager!")
        label.pack(pady=20)

        exit_button = ttk.Button(self, text="Exit", command=self.destroy)
        exit_button.pack(pady=10)

        # TODO: Add your real snippet GUI code here

if __name__ == "__main__":
    # If you directly run snippet_manager.py (for testing)
    app = SnippetManager()
    app.mainloop()
