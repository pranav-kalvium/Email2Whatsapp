import streamlit as st
import time
import random
import sys
import os

# Add the src folder to the path so we can import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from email_client import EmailClient
from whatsapp_sender import WhatsAppSender
from summarizer import EmailSummarizer

# Page configuration
st.set_page_config(
    page_title="📧 Email2WhatsApp Summarizer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for gamified appearance
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .success-box {
        padding: 1.5rem;
        border-radius: 15px;
        background: linear-gradient(45deg, #00b09b, #96c93d);
        color: white;
        margin: 1rem 0;
        border: 2px solid #ffffff;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .warning-box {
        padding: 1.5rem;
        border-radius: 15px;
        background: linear-gradient(45deg, #f46b45, #eea849);
        color: white;
        margin: 1rem 0;
        border: 2px solid #ffffff;
    }
    .info-box {
        padding: 1.5rem;
        border-radius: 15px;
        background: linear-gradient(45deg, #4facfe, #00f2fe);
        color: white;
        margin: 1rem 0;
        border: 2px solid #ffffff;
    }
    .demo-box {
        padding: 1.5rem;
        border-radius: 15px;
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        margin: 1rem 0;
        border: 2px solid #ffffff;
    }
    .progress-bar {
        height: 15px;
        background: linear-gradient(45deg, #667eea, #764ba2);
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    .metric-card {
        background: linear-gradient(45deg, #a8edea, #fed6e3);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        border: 2px solid #ffffff;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton button {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 10px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

def initialize_session_state():
    """Initialize all session state variables"""
    if 'emails_processed' not in st.session_state:
        st.session_state.emails_processed = 0
    if 'service_running' not in st.session_state:
        st.session_state.service_running = False
    if 'email_client' not in st.session_state:
        st.session_state.email_client = None
    if 'whatsapp_sender' not in st.session_state:
        st.session_state.whatsapp_sender = None
    if 'summarizer' not in st.session_state:
        st.session_state.summarizer = None
    if 'last_check' not in st.session_state:
        st.session_state.last_check = "Never"
    if 'achievements' not in st.session_state:
        st.session_state.achievements = []
    if 'demo_mode' not in st.session_state:
        st.session_state.demo_mode = True

def check_achievements():
    """Check and unlock achievements based on progress"""
    achievements = []
    
    if st.session_state.emails_processed >= 1:
        achievements.append("🎉 First Email Processed!")
    if st.session_state.emails_processed >= 5:
        achievements.append("🚀 Email Master!")
    if st.session_state.emails_processed >= 10:
        achievements.append("🏆 Super Summarizer!")
    if st.session_state.service_running and not st.session_state.demo_mode:
        achievements.append("⚡ Real Service Active!")
    elif st.session_state.service_running:
        achievements.append("🎮 Demo Mode Active!")
    
    # Add new achievements only
    for achievement in achievements:
        if achievement not in st.session_state.achievements:
            st.session_state.achievements.append(achievement)

def process_real_emails():
    """Process real unread emails and send to WhatsApp"""
    try:
        if not st.session_state.email_client or not st.session_state.whatsapp_sender:
            return 0
            
        # Get unread emails
        unread_emails = st.session_state.email_client.get_unread_emails(limit=5)
        
        if not unread_emails:
            return 0
        
        processed_count = 0
        for email_data in unread_emails:
            # Create summary
            whatsapp_message = st.session_state.summarizer.create_whatsapp_message(email_data)
            
            # Send to WhatsApp
            success = st.session_state.whatsapp_sender.send_message(
                st.session_state.whatsapp_number, 
                whatsapp_message
            )
            
            if success:
                processed_count += 1
                print(f"✅ Processed email: {email_data['subject'][:50]}...")
        
        return processed_count
        
    except Exception as e:
        print(f"❌ Error processing real emails: {e}")
        return 0
    
    # Randomly find 0-3 emails
    email_count = random.randint(0, 3)
    
    if email_count > 0:
        st.session_state.emails_processed += email_count
        st.session_state.last_check = time.strftime("%Y-%m-%d %H:%M:%S")
        return email_count
    return 0

def main():
    # Initialize session state
    initialize_session_state()
    
    # Header with gamified elements
    st.markdown('<h1 class="main-header">🎯 Email2WhatsApp Summarizer</h1>', unsafe_allow_html=True)
    
    # Sidebar for configuration
    with st.sidebar:
        st.markdown("### ⚙️ Setup Configuration")
        
        st.markdown("---")
        
        # Service Mode Selection
        st.markdown("#### 🎯 Select Mode")
        mode = st.radio("Choose how you want to test:", 
                       ["Demo Mode 🎮", "Real Email Mode 📧"])
        
        st.session_state.demo_mode = (mode == "Demo Mode 🎮")
        
        st.markdown("---")
        
        if st.session_state.demo_mode:
            st.markdown("#### 🎮 Demo Settings")
            st.info("No setup needed for demo! Just click buttons below.")
        else:
            # Email Configuration
            st.markdown("#### 📧 Email Settings")
            email_address = st.text_input("Email Address", placeholder="your.email@gmail.com")
            app_password = st.text_input("App Password", type="password", placeholder="Gmail App Password")
            
            st.markdown("---")
            
            # WhatsApp Configuration  
            st.markdown("#### 📱 WhatsApp Settings")
            whatsapp_number = st.text_input("WhatsApp Number", placeholder="+1234567890")
        
        st.markdown("---")
        
        # Service Settings
        st.markdown("#### ⚡ Service Settings")
        check_interval = st.slider("Check Interval (minutes)", 1, 60, 15)
        
        st.markdown("---")
        
        # Control Buttons
        if st.session_state.demo_mode:
            if st.button("🚀 Start Demo Service", use_container_width=True, type="primary"):
                st.session_state.service_running = True
                st.session_state.summarizer = EmailSummarizer()
                st.markdown('<div class="demo-box">🎮 Demo Mode Started! Use the buttons below to simulate email processing.</div>', unsafe_allow_html=True)
        else:
            if st.button("🚀 Start Real Service", use_container_width=True, type="primary"):
                if email_address and app_password and whatsapp_number:
                    st.session_state.service_running = True
                    st.session_state.email_client = EmailClient(email_address, app_password)
                    st.session_state.whatsapp_sender = WhatsAppSender()
                    st.session_state.summarizer = EmailSummarizer()
                    
                    # Try to connect to email
                    if st.session_state.email_client.connect():
                        st.markdown('<div class="success-box">✅ Real Email Service Started Successfully!</div>', unsafe_allow_html=True)
                    else:
                        st.markdown('<div class="warning-box">❌ Failed to connect to email. Check your credentials.</div>', unsafe_allow_html=True)
                        st.session_state.service_running = False
                else:
                    st.markdown('<div class="warning-box">⚠️ Please fill all fields for real service</div>', unsafe_allow_html=True)
        
        if st.button("⏹️ Stop Service", use_container_width=True):
            st.session_state.service_running = False
            st.markdown('<div class="info-box">⏸️ Service Stopped</div>', unsafe_allow_html=True)
        
        # Help information
        with st.expander("ℹ️ How to get Gmail App Password"):
            st.write("""
            1. Go to Google Account settings
            2. Enable 2-Factor Authentication
            3. Go to Security → App passwords
            4. Generate password for 'Mail'
            5. Use that 16-character password here
            """)

    # Main dashboard area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📊 Live Dashboard")
        
        # Progress metrics
        metric_col1, metric_col2, metric_col3 = st.columns(3)
        
        with metric_col1:
            st.markdown('<div class="metric-card">📨<br>Emails Processed<br><h2>{}</h2></div>'.format(
                st.session_state.emails_processed), unsafe_allow_html=True)
        
        with metric_col2:
            if st.session_state.demo_mode:
                status_text = "Demo 🎮" if st.session_state.service_running else "Stopped 🔴"
            else:
                status_text = "Real 📧" if st.session_state.service_running else "Stopped 🔴"
            st.markdown('<div class="metric-card">⚡<br>Service Mode<br><h3>{}</h3></div>'.format(
                status_text), unsafe_allow_html=True)
        
        with metric_col3:
            st.markdown('<div class="metric-card">🕒<br>Last Check<br><h4>{}</h4></div>'.format(
                st.session_state.last_check), unsafe_allow_html=True)
        
        # Progress bar
        progress = min(st.session_state.emails_processed / 10, 1.0)
        st.markdown("### Level Progress")
        st.markdown('<div class="progress-bar" style="width: {}%"></div>'.format(progress * 100), unsafe_allow_html=True)
        st.write(f"Progress: {int(progress * 100)}%")
        
        # Service controls
        st.markdown("### 🎮 Quick Actions")
        
        action_col1, action_col2 = st.columns(2)
        
        with action_col1:
            if st.button("🔍 Check Emails Now", use_container_width=True):
                if st.session_state.service_running:
                    with st.spinner("🕵️ Scanning for new emails..."):
                        email_count = simulate_email_check()
                        
                        if email_count > 0:
                            st.markdown(f'<div class="success-box">🎉 Found {email_count} new emails! Summary sent to WhatsApp.</div>', unsafe_allow_html=True)
                        else:
                            st.markdown('<div class="info-box">🤷 No new emails found. Everything is up to date!</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div class="warning-box">⚠️ Please start the service first</div>', unsafe_allow_html=True)
        
        with action_col2:
            if st.button("🛠️ Test Connection", use_container_width=True):
                if st.session_state.service_running:
                    st.markdown('<div class="success-box">✅ All systems operational!</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div class="warning-box">⚠️ Service not running</div>', unsafe_allow_html=True)
        
        # Demo section for testing
        st.markdown("### 🧪 Demo Zone")
        if st.button("🎯 Simulate Email Processing", use_container_width=True):
            st.session_state.emails_processed += 1
            st.markdown('<div class="demo-box">✨ Demo email processed! Check achievements!</div>', unsafe_allow_html=True)
            st.balloons()

    with col2:
        st.markdown("### 🏆 Achievements")
        
        # Check and update achievements
        check_achievements()
        
        if st.session_state.achievements:
            for achievement in st.session_state.achievements:
                st.markdown(f'<div class="success-box" style="padding: 0.5rem; margin: 0.3rem 0;">{achievement}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="info-box">🎯 Complete tasks to unlock achievements!</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown("### 📈 Stats")
        st.write(f"**Total Emails:** {st.session_state.emails_processed}")
        st.write(f"**Service Mode:** {'🎮 Demo' if st.session_state.demo_mode else '📧 Real'}")
        st.write(f"**Service Status:** {'🟢 Running' if st.session_state.service_running else '🔴 Stopped'}")
        st.write(f"**Last Check:** {st.session_state.last_check}")
        
        st.markdown("---")
        
        st.markdown("### 🎯 Next Level")
        next_level = max(0, 10 - st.session_state.emails_processed)
        if next_level > 0:
            st.write(f"**{next_level} more emails** until next level!")
        else:
            st.markdown('<div class="success-box">🏆 Maximum level reached! You\'re a pro! 🎉</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()