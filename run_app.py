import sys
import os
import subprocess

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    print("🚀 Starting Email2WhatsApp Summarizer...")
    print("📧 A beautiful app will open in your browser shortly!")
    print("⏳ Please wait...")
    
    # Run the Streamlit app using subprocess (works with all Streamlit versions)
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "src/main.py"])
    except KeyboardInterrupt:
        print("\n👋 App closed by user")
    except Exception as e:
        print(f"❌ Error starting app: {e}")
        print("💡 Try running: streamlit run src/main.py")

if __name__ == "__main__":
    main()
