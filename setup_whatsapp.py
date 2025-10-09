# setup_whatsapp.py - Run this once
import webbrowser
import time

print("🎯 WhatsApp Web Setup")
print("=" * 40)
print("This will open WhatsApp Web in your browser.")
print("Please keep this tab OPEN for the monitor to work.")
print("=" * 40)

input("Press Enter to open WhatsApp Web...")

webbrowser.open("https://web.whatsapp.com")

print("✅ WhatsApp Web opened!")
print("⏳ Please wait for it to load completely...")
print("📱 Scan the QR code if needed")
print("💡 Once loaded, keep this tab OPEN and run: python monitor_emails.py")

time.sleep(10)
print("\n✅ Setup complete! You can now run the monitor.")