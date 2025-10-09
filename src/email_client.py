# src/email_client.py - COMPLETE FIXED VERSION
import imaplib
import email
from email.header import decode_header
import logging

class EmailClient:
    def __init__(self, email_address, password, imap_server="imap.gmail.com"):
        self.email_address = email_address
        self.password = password
        self.imap_server = imap_server
        self.logger = logging.getLogger(__name__)
        
    def connect(self):
        """Connect to email server safely"""
        try:
            print(f"🔗 Connecting to {self.imap_server}...")
            self.mail = imaplib.IMAP4_SSL(self.imap_server)
            self.mail.login(self.email_address, self.password)
            print("✅ Successfully connected to email server")
            return True
        except imaplib.IMAP4.error as e:
            print(f"❌ Login failed: {str(e)}")
            print("💡 Check your email and app password")
            return False
        except Exception as e:
            print(f"❌ Connection error: {str(e)}")
            return False
    
    def get_unread_emails(self, limit=10):
        """Get unread emails with proper error handling - INCREASED LIMIT"""
        try:
            self.mail.select("inbox")
            status, messages = self.mail.search(None, 'UNSEEN')
            
            if status != "OK":
                return []
            
            email_ids = messages[0].split()
            recent_emails = email_ids[-limit:]  # Get latest emails
            
            emails_data = []
            for email_id in recent_emails:
                email_data = self._fetch_email_data(email_id)
                if email_data:
                    emails_data.append(email_data)
            
            return emails_data
            
        except Exception as e:
            print(f"❌ Error fetching emails: {str(e)}")
            return []
    
    def _fetch_email_data(self, email_id):
        """Extract email content safely"""
        try:
            status, msg_data = self.mail.fetch(email_id, "(RFC822)")
            
            if status != "OK":
                return None
            
            msg = email.message_from_bytes(msg_data[0][1])
            
            # Decode subject
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding if encoding else "utf-8")
            
            # Get email body
            body = self._extract_body(msg)
            
            return {
                "subject": subject,
                "from": msg.get("From", ""),
                "body": body,
                "date": msg.get("Date", "")
            }
            
        except Exception as e:
            print(f"❌ Error parsing email: {str(e)}")
            return None
    
    def _extract_body(self, msg):
        """Extract plain text from email body"""
        try:
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        return part.get_payload(decode=True).decode()
            else:
                return msg.get_payload(decode=True).decode()
            
            return "No readable content found"
        except:
            return "Could not extract email content"

# Test function
def test_email_client():
    print("🧪 Testing email client...")
    # This is just a test - we'll add real credentials later
    client = EmailClient("test@test.com", "test")
    print("✅ Email client created successfully!")
    print("🔗 Testing connect method...")
    result = client.connect()
    print(f"Connect result: {result}")

if __name__ == "__main__":
    test_email_client()