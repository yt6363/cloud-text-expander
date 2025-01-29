# cloud-text-expander
A powerful text expansion tool with AI integration (OpenAI/Gemini), date/time shortcuts, and clipboard automation.

📌 Cloud Text Expander
 ├── 🏠 Main Components
 │   ├── 🎨 GUI (Tkinter)
 │   │   ├── Snippet Management
 │   │   │   ├── Add Snippet
 │   │   │   ├── Edit Snippet
 │   │   │   ├── Delete Snippet
 │   │   │   ├── View Saved Snippets
 │   │   ├── AI Integration Settings
 │   │   │   ├── OpenAI API Key Input
 │   │   │   ├── Gemini API Key Input
 │   │   │   ├── Save/Delete API Key
 │   │   ├── Theme Selection
 │   │   │   ├── Dark Mode
 │   │   │   ├── Light Mode
 │   │   │   ├── System Default
 │
 │   ├── 🖥️ Key Listener (pynput)
 │   │   ├── Detect Shortcuts
 │   │   │   ├── Custom User Snippets
 │   │   │   ├── Predefined Snippets
 │   │   │   │   ├── @@date → Inserts Date
 │   │   │   │   ├── @@time → Inserts Time
 │   │   │   │   ├── @@ask [Query] → AI Response
 │   │   ├── Clipboard Automation (pyperclip)
 │   │   │   ├── Copy Shortcut Replacement
 │   │   │   ├── Paste to Active Window
 │
 │   ├── 📂 Database (Firebase / Local JSON)
 │   │   ├── Store Snippets Locally
 │   │   ├── Retrieve Snippets
 │   │   ├── Sync with Cloud (Optional)
 │
 ├── 🤖 AI Integration
 │   ├── OpenAI
 │   │   ├── GPT-4o-mini
 │   │   ├── Customizable Prompting
 │   │   ├── API Key Management
 │   ├── Google Gemini
 │   │   ├── Gemini-Pro Model
 │   │   ├── Text-Based Responses
 │   │   ├── API Key Storage
 │
 ├── ⚙️ Configuration
 │   ├── Local Storage (`~/.text_expander_config.json`)
 │   ├── API Key Handling
 │   ├── User Preferences
 │
 ├── 🛠️ Installation & Setup
 │   ├── Virtual Environment (`venv`)
 │   ├── Installing Dependencies (`pip install -r requirements.txt`)
 │   ├── Running the App (`python main.py`)
 │
 ├── 🔍 Troubleshooting
 │   ├── AI Not Responding
 │   ├── Key Listener Issues (macOS/Windows/Linux)
 │   ├── Tkinter Errors
 │   ├── Clipboard Issues
 │
 ├── 🚀 Future Enhancements
 │   ├── Browser Extension
 │   ├── Multi-Language Support
 │   ├── Sync Across Devices
 │


📖 Table of Contents
🔧 Features
📦 Installation
🚀 Usage
🧠 AI Integration
📝 Adding Snippets
💡 Available Shortcuts
🔧 Configuration
🐞 Troubleshooting
📜 License
🔧 Features
✅ Custom Text Expansion: Type @@email → Expands to youremail@example.com.
✅ Date & Time Shortcuts: @@date → 2025-01-29 | @@time → 14:35:10.
✅ AI-Powered Chatbot: @@ask What is Python? → AI-generated answer.
✅ Clipboard Automation: Instantly pastes expansions where you type.
✅ Cross-Platform Support: Works on macOS, Linux, and Windows (requires admin).
✅ Secure API Key Storage: Saves API keys locally without exposing them.

📦 Installation
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/yt6363/cloud-text-expander.git
cd cloud-text-expander
2️⃣ Create a Virtual Environment
bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# OR
.venv\Scripts\activate  # Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🚀 Usage
Run the Application
bash
Copy
Edit
python main.py
A GUI window opens, allowing you to manage snippets.
Type your shortcuts anywhere, and they will expand automatically!
🧠 AI Integration
You can use OpenAI (GPT-4) or Google Gemini AI for quick AI-powered responses.

1️⃣ Set Up an API Key
Open the app GUI → Go to the AI Settings section.
Paste your OpenAI/Gemini API key and save it.
2️⃣ How to Use AI Shortcuts
Type: @@ask What is AI?
Press Space
AI response replaces the text.
💡 AI Model Used: gpt-4o-mini (OpenAI) / gemini-pro (Google Gemini).

📝 Adding Snippets
📌 Using the GUI
Open Snippet Manager from main.py.
Click "Add Snippet", enter:
Shortcut: @@email
Expansion: youremail@example.com
Save and use anywhere!
📌 Manually Adding Snippets
Edit db.py and add:

python
Copy
Edit
snippets = {
    "@@phone": "+1 (555) 123-4567",
    "@@website": "https://example.com"
}
💡 Available Shortcuts
Shortcut	Expands To
@@date	Current date (YYYY-MM-DD)
@@time	Current time (HH:MM:SS)
@@ask ...	AI-generated response
@@email	Your saved email
@@phone	Your phone number
🔧 Configuration
📌 Where is the API Key Stored?
Stored locally in:
bash
Copy
Edit
~/.text_expander_config.json
To delete the key:
bash
Copy
Edit
rm ~/.text_expander_config.json
🐞 Troubleshooting
❌ AI isn't responding
Ensure you have an active OpenAI/Gemini API key.
Check logs for errors:
bash
Copy
Edit
tail -f logs.txt
❌ Key listener not working
macOS: Grant Accessibility Permissions (System Preferences → Security & Privacy → Input Monitoring).
Windows/Linux: Run as Administrator.
❌ Tkinter AI prompt crashes
Make sure Tkinter is installed:
bash
Copy
Edit
pip install tk
📜 License
MIT License
© 2025 Your Name. Feel free to use and modify.

🎉 Enjoy Your AI-Powered Text Expander! 🚀
For feature requests, issues, or contributions, open a pull request on GitHub.
