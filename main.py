import threading
from gui import SnippetManager
from key_listener import detect_shortcut
from auth import get_user_id

def main():
    # Start the key listener in a separate daemon thread
    listener_thread = threading.Thread(target=detect_shortcut, daemon=True)
    listener_thread.start()
    print("DEBUG: Key listener thread started.")

    # Start the GUI
    print("DEBUG: Creating GUI.")
    user_id = get_user_id()
    app = SnippetManager(user_id)
    app.mainloop()

if __name__ == "__main__":
    main()
