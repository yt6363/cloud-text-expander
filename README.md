Cloud Text Expander
A powerful text expansion tool with AI integration (OpenAI/Gemini), date/time shortcuts, and clipboard automation.

Table of Contents
Features
Installation
Usage
AI Integration
Adding Snippets
Available Shortcuts
Configuration
Troubleshooting
License
Features
Custom Text Expansion: Type @@email → Expands to youremail@example.com.
Date & Time Shortcuts: @@date → 2025-01-29 | @@time → 14:35:10.
AI-Powered Chatbot: @@ask What is Python? → AI-generated answer.
Clipboard Automation: Instantly pastes expansions where you type.
Cross-Platform Support: Works on macOS, Linux, and Windows (requires admin).
Secure API Key Storage: Saves API keys locally without exposing them.
Installation
Clone the Repository:
bash
Copy
Edit
git clone https://github.com/yt6363/cloud-text-expander.git
cd cloud-text-expander
Create a Virtual Environment:
bash
Copy
Edit
python -m venv .venv  
source .venv/bin/activate  # macOS/Linux  
OR
bash
Copy
Edit
.venv\Scripts\activate  # Windows  
Install Dependencies:
bash
Copy
Edit
pip install -r requirements.txt  
Usage
Run the application:

bash
Copy
Edit
python main.py  
A GUI window opens, allowing you to manage snippets. Type your shortcuts anywhere, and they will expand automatically.

AI Integration
You can use OpenAI (GPT-4) or Google Gemini AI for quick AI-powered responses.

Set Up an API Key

Open the app GUI → Go to AI Settings.
Paste your OpenAI/Gemini API key and save it.
How to Use AI Shortcuts

Type: @@ask What is AI?
Press Space
AI response replaces the text.
AI Models Used:

OpenAI: gpt-4o-mini
Google Gemini: gemini-pro
Adding Snippets
Using the GUI
Open Snippet Manager.
Click "Add Snippet".
Enter:
Shortcut: @@email
Expansion: youremail@example.com
Save and use anywhere.
Manually Adding Snippets
Edit db.py and add:

python
Copy
Edit
snippets = {
    "@@phone": "+1 (555) 123-4567",
    "@@website": "https://example.com"
}
Available Shortcuts
Shortcut	Expands To
@@date	Current date (YYYY-MM-DD)
@@time	Current time (HH:MM:SS)
@@ask ...	AI-generated response
@@email	Your saved email
@@phone	Your phone number
Configuration
Where is the API Key Stored?
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
Troubleshooting
AI isn't responding
Ensure you have an active OpenAI/Gemini API key.
Check logs for errors:
bash
Copy
Edit
tail -f logs.txt  
Key listener not working
macOS: Grant Accessibility Permissions (System Preferences → Security & Privacy → Input Monitoring).
Windows/Linux: Run as Administrator.
Tkinter AI prompt crashes
Make sure Tkinter is installed:
bash
Copy
Edit
pip install tk  
License
MIT License © 2025 Yashwanth tatineni. Feel free to use and modify.

For feature requests, issues, or contributions, open a pull request on GitHub.
