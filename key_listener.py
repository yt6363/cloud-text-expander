import os
import time
import datetime
import pyperclip
import tkinter as tk
from tkinter import simpledialog
from pynput import keyboard
from db import get_snippets
from auth import get_user_id

# AI Configuration (Handles OpenAI or Gemini)
AI_ENABLED = False
AI_PROVIDER = None
AI_API_KEY = None

try:
    from openai_config import load_api_key
    import google.generativeai as genai
    import openai

    AI_API_KEY = load_api_key()
    
    if AI_API_KEY:
        # Detect if using OpenAI or Gemini
        try:
            openai.api_key = AI_API_KEY
            AI_PROVIDER = "OpenAI"
        except Exception:
            genai.configure(api_key=AI_API_KEY)
            AI_PROVIDER = "Gemini"
        
        AI_ENABLED = True  # Set AI flag to True

    print(f"✅ AI Enabled: {AI_ENABLED}, Provider: {AI_PROVIDER}")
except ImportError:
    print("⚠️ AI module(s) not installed. AI features disabled.")
except Exception as e:
    print(f"⚠️ AI Initialization Error: {e}")

# Stores typed keys
typed_keys = []
snippets = {}  # Loaded dynamically


def delete_shortcut(shortcut):
    """ Deletes only the snippet text without removing preceding content. """
    script = f"""
    tell application "System Events"
        repeat {len(shortcut) + 1} times
            key down shift
            key code 123 -- left arrow
            key up shift
            delay 0.05
        end repeat
        key code 51  -- Delete key
    end tell
    """
    os.system(f'osascript <<EOF\n{script}\nEOF')
    time.sleep(0.3)


def replace_with_clipboard(text):
    """ Copy text to clipboard & paste using Cmd+V. """
    pyperclip.copy(text)
    time.sleep(0.3)
    os.system("osascript -e 'tell application \"System Events\" to keystroke \"v\" using command down'")
    time.sleep(0.3)
    print(f"✅ Inserted: {text}")


def generate_ai_response(prompt):
    """ Calls AI model (OpenAI or Gemini) to generate a response. """
    if not AI_ENABLED:
        return "❌ AI is not enabled. Set API Key in GUI."

    try:
        print(f"🔍 Sending request to {AI_PROVIDER} API...")

        if AI_PROVIDER == "OpenAI":
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            return response["choices"][0]["message"]["content"].strip()

        elif AI_PROVIDER == "Gemini":
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(prompt)
            return response.text.strip()

        else:
            return "❌ Unsupported AI provider."

    except Exception as e:
        print(f"⚠️ AI Error: {e}")
        return f"⚠️ AI Error: {e}"


def ask_ai_question():
    """ Runs in the main Tkinter thread to avoid crashes. """
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    ai_question = simpledialog.askstring("AI Question", "Enter your AI prompt:")
    
    root.destroy()  # Close the Tkinter instance after getting input
    
    if ai_question:
        print(f"🧠 Sending to AI: {ai_question}")
        ai_response = generate_ai_response(ai_question)
        delete_shortcut("@@ask")  # Remove "@@ask" shortcut
        replace_with_clipboard(ai_response)
    else:
        print("❌ No input provided. Skipping AI request.")


### **Define `on_press` BEFORE Using `keyboard.Listener`**
def on_press(key):
    """ Capture typed keys """
    if hasattr(key, 'char') and key.char:
        typed_keys.append(key.char)


def on_release(key):
    """ Detect shortcuts and execute AI prompts. """
    if key == keyboard.Key.space:
        shortcut = "".join(typed_keys).strip()
        print(f"🚀 Detected shortcut: {shortcut}")

        if shortcut in snippets:
            print(f"Expanding {shortcut} -> {snippets[shortcut]}")
            delete_shortcut(shortcut)
            replace_with_clipboard(snippets[shortcut])

        elif shortcut == "@@date":
            today = datetime.date.today().strftime("%Y-%m-%d")
            print(f"📅 Expanding {shortcut} -> {today}")
            delete_shortcut(shortcut)
            replace_with_clipboard(today)

        elif shortcut == "@@time":
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"⏰ Expanding {shortcut} -> {now}")
            delete_shortcut(shortcut)
            replace_with_clipboard(now)

        elif shortcut.startswith("@@ask") and AI_ENABLED:
            print(f"🧠 AI Shortcut Detected. Using {AI_PROVIDER}...")

            # Run Tkinter dialog in main thread to prevent errors
            tk_root = tk.Tk()
            tk_root.withdraw()
            tk_root.after(100, ask_ai_question)
            tk_root.mainloop()

        typed_keys.clear()

    elif key == keyboard.Key.esc:
        return False


def detect_shortcut():
    """ Start the global keyboard listener. """
    global snippets
    user_id = get_user_id()
    snippets = get_snippets(user_id)
    print("🔥 Loaded snippets:", snippets)

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    detect_shortcut()
