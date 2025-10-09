# src/whatsapp_sender.py - FIXED VERSION
import pywhatkit
import time
import logging
import webbrowser
import threading

class WhatsAppSender:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.whatsapp_ready = False
        self.setup_done = False
    
    def setup_whatsapp_web(self):
        """Setup WhatsApp Web - RUN ONLY ONCE"""
        if self.setup_done:
            return True
            
        try:
            print("🔍 Setting up WhatsApp Web...")
            webbrowser.open("https://web.whatsapp.com")
            print("✅ WhatsApp Web opened in browser")
            print("⏳ Waiting 20 seconds for page to load completely...")
            
            # Wait for WhatsApp Web to load
            for i in range(20, 0, -1):
                print(f"   Loading... {i} seconds remaining", end='\r')
                time.sleep(1)
            print("\n✅ WhatsApp Web should be ready now!")
            
            self.setup_done = True
            self.whatsapp_ready = True
            return True
            
        except Exception as e:
            print(f"❌ Could not setup WhatsApp Web: {e}")
            return False
    
    def wait_for_whatsapp_ready(self):
        """Wait until WhatsApp Web is ready to send messages"""
        if not self.whatsapp_ready:
            print("⏳ Waiting for WhatsApp Web to be ready...")
            time.sleep(10)
            self.whatsapp_ready = True
    
    def send_message(self, phone_number, message, delay_between_messages=10):
        """Send message with proper queueing and delays"""
        try:
            print(f"📱 Preparing to send message to {phone_number}")
            
            # Wait if previous message is still processing
            self.wait_for_whatsapp_ready()
            
            print("⚡ Sending message now...")
            
            # Send message instantly
            pywhatkit.sendwhatmsg_instantly(
                phone_no=phone_number,
                message=message,
                wait_time=10,  # Reduced wait time
                tab_close=False,  # Keep tab open
                close_time=8
            )
            
            print("✅ WhatsApp message sent successfully!")
            
            # Add delay before next message can be sent
            print(f"⏳ Waiting {delay_between_messages} seconds before next message...")
            time.sleep(delay_between_messages)
            
            return True
            
        except Exception as e:
            print(f"❌ WhatsApp error: {str(e)}")
            print("💡 Tips:")
            print("   - Make sure WhatsApp Web is loaded")
            print("   - Don't touch computer while sending")
            print("   - Keep browser window visible")
            return False

# Test function
def test_whatsapp_sender():
    print("🧪 Testing FIXED WhatsApp sender...")
    sender = WhatsAppSender()
    
    # Setup once
    sender.setup_whatsapp_web()
    
    # Test sending
    test_number = "+918409841906"  # Your number
    test_message = "🚀 Test from FIXED WhatsApp sender!"
    
    success = sender.send_message(test_number, test_message)
    if success:
        print("🎉 Fixed version working correctly!")

if __name__ == "__main__":
    test_whatsapp_sender()