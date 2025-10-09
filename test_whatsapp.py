# test_whatsapp.py (updated sending part)
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from whatsapp_sender import WhatsAppSender
import time
import pywhatkit

def test_whatsapp():
    print("🎯 WhatsApp Messaging Test")
    print("=" * 40)
    
    # Create sender instance
    sender = WhatsAppSender()
    
    # Get your phone number
    print("\n📱 Enter your WhatsApp number with country code:")
    print("   Example: +91XXXXXXXXXX for India")
    print("   Example: +1XXXXXXXXXX for US")
    
    phone_number = input("👉 Enter your number: ").strip()
    
    # Validate number format
    if not phone_number.startswith('+'):
        print("❌ Please include country code starting with +")
        return
    
    # Test message
    test_message = """🚀 *TEST MESSAGE from Your Email2WhatsApp App!*

🎉 Congratulations! Your WhatsApp integration is WORKING!

📧 This means your app can now:
   • Send email summaries to WhatsApp
   • Automate notifications  
   • Keep you updated anywhere

⏰ Sent at: {time}

🎯 Next: Let's connect real email!""".format(time=time.strftime("%Y-%m-%d %H:%M:%S"))
    
    print(f"\n📝 Test message prepared:")
    print(f"   To: {phone_number}")
    print(f"   Length: {len(test_message)} characters")
    
    print("\n⚠️  IMPORTANT: Make sure:")
    print("   1. You're logged into WhatsApp Web in your browser")
    print("   2. Your browser window is visible (not minimized)")
    print("   3. You have internet connection")
    
    input("\n🎯 Press Enter to send test message INSTANTLY...")
    
    print("\n⚡ Sending message INSTANTLY...")
    print("   Browser will open in 10 seconds...")
    print("   Please don't touch your computer!")
    
    # Use INSTANT sending instead
    try:
        pywhatkit.sendwhatmsg_instantly(
            phone_no=phone_number,
            message=test_message,
            wait_time=15,
            tab_close=True
        )
        print("\n🎉 🎉 🎉 SUCCESS! 🎉 🎉 🎉")
        print("✅ WhatsApp message sent successfully!")
        print("✅ Check your WhatsApp on your phone!")
        print("✅ Your app is now POWERED with real messaging!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("💡 Let's try the manual method...")
        manual_whatsapp_test(phone_number, test_message)

def manual_whatsapp_test(phone_number, message):
    """Fallback method if automatic fails"""
    print("\n🔄 Trying manual method...")
    print("1. Opening WhatsApp Web manually...")
    
    # Open WhatsApp Web
    pywhatkit.open_web()
    time.sleep(5)
    
    print("2. Please MANUALLY select the chat and paste this message:")
    print("\n" + "="*50)
    print(message)
    print("="*50)
    
    print("\n3. Send the message manually")
    print("4. Then come back here to continue!")
    
    input("\nPress Enter after you've sent the message manually...")
    print("🎉 Great! Manual test completed!")

if __name__ == "__main__":
    test_whatsapp()