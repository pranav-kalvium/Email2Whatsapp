# 📧 Email2WhatsApp Summarizer

A powerful Python application that automatically monitors your Gmail inbox, generates **AI-powered summaries** of new emails, and sends them directly to your WhatsApp.  
Stay updated on the go — no more constantly checking your inbox!

---

## 🚀 Features

- **Smart Email Monitoring** – Continuously checks your Gmail for new messages  
- **AI-Powered Summarization** – Uses NLP to produce concise, meaningful summaries  
- **WhatsApp Integration** – Automatically delivers summaries to your WhatsApp  
- **Beautiful Dashboard** – Streamlit-based interface with progress tracking and gamification  
- **24/7 Automation** – Runs seamlessly in the background with custom intervals  
- **Universal Compatibility** – Works with any Gmail and WhatsApp account

---

## 🛠️ Installation

### ✅ Prerequisites

- Python **3.7+**
- Gmail account with **2-factor authentication enabled**
- WhatsApp account
- Chrome, Edge, or Firefox browser installed

---

### ⚙️ Step-by-Step Setup

#### 1. Clone the repository

```bash
git clone https://github.com/yourusername/email_whatsapp_summarizer.git
cd email_whatsapp_summarizer
2. Install dependencies
bash
Copy code
pip install -r requirements.txt
3. Setup Gmail App Password
Go to Google Account → Security

Enable 2-Factor Authentication

Open App passwords

Generate a password for Mail

Copy the 16-character password

📖 Usage
🔹 Quick Start
bash
Copy code
# Run complete integration test
python test_full_integration.py

# Start 24/7 email monitoring
python monitor_emails.py

# Launch the web dashboard
python run_app.py
🖥️ Method 1: Web Dashboard (Recommended)
bash
Copy code
python run_app.py
Then open http://localhost:8501

Configure email & WhatsApp settings

Monitor progress in real-time

View achievements and usage statistics

💻 Method 2: Terminal Monitor
bash
Copy code
python monitor_emails.py
Runs continuously in background

Checks emails every 15 minutes

Sends summaries automatically

Displays logs and updates in terminal

🧪 Method 3: Integration Testing
bash
Copy code
python test_full_integration.py
Tests the full email → summarizer → WhatsApp flow

Confirms all components are connected correctly

⚙️ Configuration
✉️ Email Settings
Setting	Description
Gmail Address	Your full Gmail address
App Password	16-character Google App Password
Check Interval	Frequency of email checking (default: 15 minutes)

💬 WhatsApp Settings
Setting	Description
Phone Number	Include country code (e.g., 91XXXXXXXXXX for India)
Password	Not required for WhatsApp integration

🏗️ Project Structure
bash
Copy code
email_whatsapp_summarizer/
├── src/
│   ├── main.py              # Streamlit web app
│   ├── email_client.py      # Gmail integration & parsing
│   ├── whatsapp_sender.py   # WhatsApp automation
│   └── summarizer.py        # AI summarization engine
├── monitor_emails.py        # Background monitor (24/7)
├── test_full_integration.py # End-to-end system testing
├── test_whatsapp.py         # WhatsApp test module
├── test_email.py            # Email test module
├── run_app.py               # App launcher
└── requirements.txt         # Dependencies
🧠 Technical Details
📩 Email Client (email_client.py)
Secure IMAP connection to Gmail

Unread email detection

Safe reconnection handling

Robust error logging

💬 WhatsApp Sender (whatsapp_sender.py)
Automated browser control via Selenium

Multi-browser support (Chrome, Edge, Firefox)

Automatic message sending

Persistent login session management

🧠 AI Summarizer (summarizer.py)
NLP summarization using NLTK and Sumy

Smart content extraction and keyword emphasis

Fallback strategies for robust performance

🌐 Web Interface (main.py)
Real-time Streamlit dashboard

Configuration management

Progress & achievement tracking

🐛 Troubleshooting
❌ Gmail Connection Failed
Ensure 2FA is enabled

Use App Password, not your Gmail password

Confirm IMAP is enabled in Gmail settings

❌ WhatsApp Not Sending
Make sure WhatsApp Web is open in browser

Use correct phone format (no “+”)

Keep browser window visible and active

❌ No Emails Found
Verify you have unread emails

Check spam or filters

Ensure Gmail credentials are correct

❌ Import / Module Errors
bash
Copy code
pip install -r requirements.txt
python --version  # Must be 3.7+
📋 Dependencies
ini
Copy code
selenium==4.15.0
streamlit==1.28.0
imaplib2==3.6
nltk==3.8.1
sumy==0.10.0
python-dotenv==1.0.0
schedule==1.2.0
beautifulsoup4==4.12.2
webdriver-manager==4.0.1
🔄 Maintenance
🔁 Updating the Application
bash
Copy code
git pull origin main
pip install -r requirements.txt
📊 Checking Status
Monitor logs in the terminal

Web dashboard shows live status & stats

Achievement system tracks performance

🛑 Stopping the Service
Press Ctrl + C in terminal

Close Streamlit browser tab

Restart anytime with the same commands

🎯 Use Cases
Busy Professionals – Get summaries of important emails

Remote Teams – Stay updated with work communications

Personal Productivity – No inbox distractions

Multi-Account Users – Monitor multiple Gmail accounts

📞 Support
If you face issues or have ideas:

Check the troubleshooting section

Review code comments

Open a GitHub issue with detailed description

📄 License
This project is open-source under the MIT License.
You’re free to use, modify, and share it with attribution.
