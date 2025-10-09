# whatsapp_reminder.py
import webbrowser
import time

def ensure_whatsapp_web():
    print("🔔 WhatsApp Web Check")
    print("Opening WhatsApp Web in your browser...")
    
    # Open WhatsApp Web
    webbrowser.open("https://web.whatsapp.com")
    
    print("⏳ Please wait for WhatsApp Web to load...")
    time.sleep(10)
    
    print("✅ WhatsApp Web should be ready!")
    print("💡 Keep this browser tab open for automatic messaging")
    
    input("Press Enter when WhatsApp Web is loaded and ready...")
    return True

if __name__ == "__main__":
    ensure_whatsapp_web()