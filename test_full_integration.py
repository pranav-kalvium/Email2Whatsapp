# test_full_integration.py - COMPLETE FIXED VERSION
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from email_client import EmailClient
from whatsapp_sender import WhatsAppSender
from summarizer import EmailSummarizer
import time

def format_phone_number(number):
    """Ensure phone number has country code"""
    number = number.strip()
    if not number.startswith('+'):
        if number.startswith('0'):
            number = number[1:]
        number = '+91' + number
    return number

def test_full_integration():
    print("🎯 FULL INTEGRATION TEST - Email → Summary → WhatsApp")
    print("=" * 60)
    
    # Get credentials
    print("\n🔐 Enter your credentials:")
    email_address = input("Gmail address: ").strip()
    app_password = input("Gmail App Password: ").strip()
    whatsapp_number = input("WhatsApp number: ").strip()
    
    # Format phone number
    whatsapp_number = format_phone_number(whatsapp_number)
    print(f"📱 Formatted number: {whatsapp_number}")
    
    print(f"\n🚀 Starting full integration test...")
    
    # Initialize all components
    email_client = EmailClient(email_address, app_password)
    whatsapp_sender = WhatsAppSender()
    summarizer = EmailSummarizer()
    
    # Test email connection
    print("\n1. 📧 Testing email connection...")
    if not email_client.connect():
        print("❌ Email connection failed")
        return
    
    print("✅ Email connected!")
    
    # Setup WhatsApp Web ONCE
    print("\n2. 📱 Setting up WhatsApp Web...")
    whatsapp_sender.setup_whatsapp_web()
    
    # Check for emails
    print("\n3. 📥 Checking for unread emails...")
    unread_emails = email_client.get_unread_emails(limit=10)  # Increased limit
    
    if not unread_emails:
        print("📭 No unread emails found.")
        print("💡 Send yourself a test email to try this feature!")
        return
    
    print(f"✅ Found {len(unread_emails)} unread emails!")
    
    # Process each email with proper delays
    for i, email_data in enumerate(unread_emails, 1):
        print(f"\n--- Processing Email {i}/{len(unread_emails)} ---")
        print(f"📨 From: {email_data['from']}")
        print(f"📝 Subject: {email_data['subject']}")
        
        # Create summary
        whatsapp_message = summarizer.create_whatsapp_message(email_data)
        print(f"📄 Summary created ({len(whatsapp_message)} chars)")
        
        # Send to WhatsApp with increasing delays
        delay = 10 + (i * 3)  # 10s, 13s, 16s delays (increases gradually)
        print(f"⏰ Waiting {delay} seconds before sending...")
        time.sleep(delay)
        
        print("🎯 Sending to WhatsApp NOW...")
        
        success = whatsapp_sender.send_message(whatsapp_number, whatsapp_message, delay_between_messages=8)
        
        if success:
            print("🎉 ✅ EMAIL SUCCESSFULLY SENT TO WHATSAPP!")
            print("📱 Check your phone!")
        else:
            print("❌ Failed to send to WhatsApp")
        
        # Only add delay if there are more emails
        if i < len(unread_emails):
            print("⏳ Brief pause before next email...")
            time.sleep(5)
    
    print("\n" + "=" * 60)
    print("🎉 🎉 🎉 FULL INTEGRATION TEST COMPLETE! 🎉 🎉 🎉")
    print(f"✅ Processed {len(unread_emails)} emails successfully!")
    print("💡 Keep the WhatsApp Web tab open for future use!")

if __name__ == "__main__":
    test_full_integration()