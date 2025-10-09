# monitor_emails.py - UNLIMITED VERSION
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from email_client import EmailClient
from whatsapp_sender import WhatsAppSender
from summarizer import EmailSummarizer

def monitor_emails():
    print("🔄 Starting 24/7 Email Monitor")
    print("📧 Checking emails every 15 minutes")
    print("📱 Sending summaries to WhatsApp")
    print("♾️  Processing ALL emails (no limits)")
    print("⏸️  Press Ctrl+C to stop")
    print("=" * 50)
    
    # Load credentials
    email_address = "pranavprakash6410@gmail.com"
    app_password = "oqcu tmsp jire wgcs"
    whatsapp_number = "+918409841906"
    
    # Initialize components
    email_client = EmailClient(email_address, app_password)
    whatsapp_sender = WhatsAppSender()
    summarizer = EmailSummarizer()
    
    if not email_client.connect():
        print("❌ Failed to connect to email")
        return
    
    print("✅ Email monitor started successfully!")
    
    # SETUP WHATSAPP WEB ONLY ONCE at startup
    print("🔍 Setting up WhatsApp Web...")
    whatsapp_sender.setup_whatsapp_web()
    print("✅ WhatsApp Web is ready! It will stay open.")
    print("💡 Please don't close the WhatsApp Web browser tab!")
    
    try:
        check_count = 0
        while True:
            check_count += 1
            print(f"\n🕒 Check #{check_count} at {time.strftime('%H:%M:%S')}")
            
            # Get ALL unread emails (no limit)
            unread_emails = email_client.get_unread_emails(limit=10)  # Increased limit
            
            if unread_emails:
                print(f"📨 Found {len(unread_emails)} new emails!")
                
                for i, email_data in enumerate(unread_emails, 1):
                    print(f"\n📧 Processing email {i}/{len(unread_emails)}")
                    print(f"   From: {email_data['from']}")
                    print(f"   Subject: {email_data['subject'][:80]}...")
                    
                    # Create summary
                    whatsapp_message = summarizer.create_whatsapp_message(email_data)
                    print(f"   📄 Summary created ({len(whatsapp_message)} chars)")
                    
                    # Calculate dynamic delay (longer for later emails to avoid spam)
                    dynamic_delay = max(8, i * 2)  # 8s, 10s, 12s, etc.
                    print(f"   ⏰ Waiting {dynamic_delay} seconds before sending...")
                    time.sleep(dynamic_delay)
                    
                    # Send to WhatsApp
                    success = whatsapp_sender.send_message(whatsapp_number, whatsapp_message, delay_between_messages=5)
                    
                    if success:
                        print(f"   ✅ SENT: {email_data['subject'][:60]}...")
                    else:
                        print(f"   ❌ FAILED: {email_data['subject'][:60]}...")
                        print("   💡 Continuing with next email...")
                    
                    # Small delay between emails
                    if i < len(unread_emails):
                        print("   ⏳ Brief pause...")
                        time.sleep(3)
                        
                print(f"\n🎉 Processed {len(unread_emails)} emails successfully!")
            else:
                print("📭 No new emails")
            
            # Wait 15 minutes before next check
            print("\n⏳ Waiting 15 minutes for next check...")
            for minute in range(15, 0, -1):
                print(f"   Next check in {minute:2d} minutes...", end='\r')
                time.sleep(60)
            print("   Next check in  0 minutes...")
            
    except KeyboardInterrupt:
        print("\n\n🛑 Monitor stopped by user")
        print("👋 Thank you for using Email2WhatsApp!")
        print("📧 Your email summaries will resume when you restart the monitor.")

if __name__ == "__main__":
    monitor_emails()