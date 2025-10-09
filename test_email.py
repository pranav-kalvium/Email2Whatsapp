# test_email.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from email_client import EmailClient
from summarizer import EmailSummarizer

def test_email():
    print("📧 Real Email Connection Test")
    print("=" * 50)
    
    print("\n🔐 Enter your Gmail credentials:")
    email_address = input("👉 Your Gmail address: ").strip()
    app_password = input("👉 Gmail App Password (16 chars): ").strip()
    
    print(f"\n🔗 Testing connection to {email_address}...")
    
    # Create email client
    client = EmailClient(email_address, app_password)
    
    # Test connection
    if client.connect():
        print("✅ SUCCESS! Connected to Gmail!")
        
        # Try to get unread emails
        print("\n📥 Checking for unread emails...")
        unread_emails = client.get_unread_emails(limit=3)
        
        if unread_emails:
            print(f"🎉 Found {len(unread_emails)} unread emails!")
            
            # Test summarization
            summarizer = EmailSummarizer()
            
            for i, email_data in enumerate(unread_emails, 1):
                print(f"\n--- Email {i} ---")
                print(f"From: {email_data['from']}")
                print(f"Subject: {email_data['subject']}")
                
                # Create summary
                whatsapp_message = summarizer.create_whatsapp_message(email_data)
                print(f"Summary: {whatsapp_message[:200]}...")
                
        else:
            print("📭 No unread emails found. That's good - your inbox is clean!")
            
    else:
        print("❌ Failed to connect to Gmail.")
        print("💡 Troubleshooting tips:")
        print("   1. Make sure 2-factor authentication is ON")
        print("   2. Use the 16-character App Password (not your regular password)")
        print("   3. Check if 'Less secure app access' is enabled in Google settings")

if __name__ == "__main__":
    test_email()