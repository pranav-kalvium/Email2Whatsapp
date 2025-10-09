from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    print("📥 Downloading NLTK data...")
    nltk.download('punkt')

class EmailSummarizer:
    def __init__(self):
        self.summarizer = LsaSummarizer()
    
    def summarize_text(self, text, sentences_count=2):
        """Summarize text using LSA algorithm"""
        try:
            if len(text.split()) < 50:  # If text is too short
                return text[:200] + "..." if len(text) > 200 else text
            
            parser = PlaintextParser.from_string(text, Tokenizer("english"))
            summary = self.summarizer(parser.document, sentences_count)
            
            summary_text = " ".join(str(sentence) for sentence in summary)
            return summary_text if summary_text else "Could not generate summary"
            
        except Exception as e:
            print(f"❌ Error in summarization: {str(e)}")
            return text[:300] + "..."  # Return first 300 chars as fallback
    
    def create_whatsapp_message(self, email_data):
        """Create a formatted WhatsApp message from email data"""
        try:
            summary = self.summarize_text(email_data['body'])
            
            message = f"""📧 *New Email Summary*

*From:* {email_data['from']}
*Subject:* {email_data['subject']}

*Summary:*
{summary}

⏰ *Received:* {email_data['date']}"""
            
            return message
            
        except Exception as e:
            print(f"❌ Error creating WhatsApp message: {str(e)}")
            return f"New email from {email_data['from']}: {email_data['subject'][:100]}..."

# Test function
def test_summarizer():
    print("🧪 Testing summarizer...")
    summarizer = EmailSummarizer()
    
    test_text = """
    Hello Team, I hope this email finds you well. We have an important meeting scheduled for next Monday at 10:00 AM in the main conference room. 
    The meeting will cover our quarterly results and future projections. Please bring your reports and be prepared to discuss your department's performance. 
    We will also be discussing the upcoming product launch and marketing strategies. Your attendance is mandatory as we have critical decisions to make.
    """
    
    summary = summarizer.summarize_text(test_text)
    print("📝 Original text length:", len(test_text))
    print("📄 Summary length:", len(summary))
    print("✅ Summarizer working correctly!")
    print("Sample summary:", summary)

if __name__ == "__main__":
    test_summarizer()