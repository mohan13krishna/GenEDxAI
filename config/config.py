# GEMINI_API_KEY = "AIzaSyDllhh8PF8P27IFP6B4EGCjJ87wlhu8rUg"  # Replace with your actual Gemini API key
# MONGODB_URI = "mongodb://localhost:27017/"
# DB_NAME = "edu_chatbot"


import os
from dotenv import load_dotenv

load_dotenv()

# Try to get from Streamlit secrets first (for Cloud deployment)
try:
    import streamlit as st
    if hasattr(st, 'secrets') and 'MONGODB_URI' in st.secrets:
        MONGODB_URI = st.secrets['MONGODB_URI']
    else:
        MONGODB_URI = os.getenv("MONGODB_URI")
    if hasattr(st, 'secrets') and 'OPENROUTER_API_KEY' in st.secrets:
        OPENROUTER_API_KEY = st.secrets['OPENROUTER_API_KEY']
    else:
        OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
except:
    # Fallback if Streamlit not available (e.g., during testing)
    MONGODB_URI = os.getenv("MONGODB_URI")
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

DB_NAME = "edu_chatbot"

# Validate configuration in production
if not MONGODB_URI or MONGODB_URI == "":
    import sys
    if '/mount/src' in sys.argv[0] or os.getenv('STREAMLIT_SERVER_HEADLESS'):
        raise RuntimeError(
            "❌ MONGODB_URI not configured!\n\n"
            "To fix this in Streamlit Cloud:\n"
            "1. Go to your app's Settings (gear icon)\n"
            "2. Click 'Secrets'\n"
            "3. Add: MONGODB_URI = 'mongodb+srv://...'\n"
            "4. Save - the app will restart automatically"
        )
