#app.py

import streamlit as st
from streamlit_lottie import st_lottie
import requests
import google.generativeai as genai
from utils.auth import login_user, register_user
from utils.chatbot import get_learning_response
from utils.exam import generate_exam, evaluate_exam
from utils.db import store_result, get_user_results
from utils.db import save_chat, get_chat_history, clear_chat_history

# from fpdf import FPDF
# import io

hide_streamlit_elements = """
<style>
#GithubIcon { 
    visibility: hidden; 
}
.stDeployButton { 
    visibility: hidden; 
}
.viewerBadge_container__1QSob { 
    visibility: hidden; 
}
</style>
"""
st.markdown(hide_streamlit_elements, unsafe_allow_html=True)
# Load custom CSS
with open("static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Helper to load Lottie animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    st.session_state["username"] = None
    st.session_state["chat_history"] = []
    st.session_state["exam_active"] = False
    st.session_state["exam_questions"] = ""
    st.session_state["menu"] = "Login"

# Sidebar Navigation
st.sidebar.markdown('<h1 style="font-size:36px;">📘 EduBot</h1>', unsafe_allow_html=True)
st.sidebar.markdown('<div style="font-size:28px;">🔐 Menu</div>', unsafe_allow_html=True)

if not st.session_state["logged_in"]:
    menu = st.sidebar.radio("", ["Login", "Register"], key="menu_radio")
else:
    menu = st.sidebar.radio("📚 Menu", ["Learn", "Exam", "Results"], key="menu_radio")
    if st.sidebar.button("🚪 Logout"):
        st.session_state["logged_in"] = False
        st.session_state["username"] = None
        st.session_state["chat_history"] = []
        st.session_state["exam_active"] = False
        st.session_state["menu"] = "Login"
        st.success("✅ Logged out successfully!")
        st.rerun()

# =============================
# -------- Login Page ---------
# =============================
if menu == "Login":
    st.title("🤖 GenEDxAI")
    st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 5])
    with col1:
        st.markdown("""
        <div style="padding: 20px 0;">
            <h3>😊 Welcome to GenEDxAI!</h3>
            <p style="font-size: 18px; line-height: 1.5;">
                👋 A platform that uses AI to create educational content and evaluate your learning. 
                Whether you're a student or educator, we provide personalized support and quizzes 
                to help you succeed!
            </p>
            <p style="margin-top: 20px; font-size: 16px;">
                Please login using the sidebar to get started.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        lottie_login = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_1pxqjqps.json")
        if lottie_login:
            st_lottie(lottie_login, height=450, key="welcome_animation")
        else:
            st.warning("⚠ Could not load animation")

    # Sidebar login fields
    st.sidebar.markdown('<div style="margin-top:100px;"><label style="font-size:25px;">👤 Username</label></div>', unsafe_allow_html=True)
    login_username = st.sidebar.text_input("", key="login_user_input", placeholder="Enter username")

    st.sidebar.markdown('<div style="margin-top:30px;"><label style="font-size:25px;">🔒 Password</label></div>', unsafe_allow_html=True)
    login_password = st.sidebar.text_input("", type="password", key="login_pass_input", placeholder="Enter password")

    login_clicked = st.sidebar.button("🔐 *Login*")

    if login_clicked:
        try:
            if login_user(login_username, login_password):
                st.session_state["logged_in"] = True
                st.session_state["username"] = login_username
                st.session_state["menu"] = "Learn"
                st.success(f"✅ Logged in as {login_username}!")
                st.rerun()
            else:
                st.error("❌ Invalid username or password.")
        except Exception as e:
            st.error(f"❌ Login failed: {str(e)}")

# =============================
# ------- Register Page -------
# =============================
elif menu == "Register":
    st.title("📝 Register for EduBot")
    st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 5])
    with col1:
        st.markdown("""
        <div style="padding: 20px 0;">
            <h3>Join our learning community!</h3>
            <p style="font-size: 16px; line-height: 1.5;">
                Create your account to access personalized learning content,
                take exams, and track your progress.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        lottie_login = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_1pxqjqps.json")
        if lottie_login:
            st_lottie(lottie_login, height=450, key="register_animation")
        else:
            st.warning("⚠ Could not load animation")

    # Sidebar register fields
    st.sidebar.markdown('<div style="margin-top:100px;"><label style="font-size:25px;">👤 New Username</label></div>', unsafe_allow_html=True)
    register_username = st.sidebar.text_input("", key="register_user_input", placeholder="Choose a unique username")

    st.sidebar.markdown('<div style="margin-top:50px;"><label style="font-size:25px;">🔒 New Password</label></div>', unsafe_allow_html=True)
    register_password = st.sidebar.text_input("", type="password", key="register_pass_input", placeholder="Choose a strong password")

    register_clicked = st.sidebar.button("📝 *Register*")

    if register_clicked:
        try:
            register_user(register_username, register_password)
            st.success("✅ Registered successfully! Please log in.")
            st.session_state["menu"] = "Login"
            st.rerun()
        except Exception as e:
            st.error(f"❌ Registration failed: {str(e)}")
            
            
            
elif menu == "Learn":
    st.title(f"👋 Welcome, {st.session_state['username']}!")

    prompt = st.text_area("💬 Ask me anything to learn!")

    if st.button("🚀 Submit", key="submit_prompt"):
        if prompt:
            response = get_learning_response(prompt)
            # Append consistent keys for user and ai messages
            st.session_state["chat_history"].append({"user_msg": prompt, "ai_msg": response})
            save_chat(st.session_state["username"], prompt, response)
            st.success("✅ Response received!")

    # Get chat history safely, default empty list
    chat_history = get_chat_history(st.session_state["username"]) or []

    if chat_history:
        st.subheader("📜 Chat History")

        # Clear chat button with a unique key
        if st.button("🧹 Clear Chat History", key="clear_history"):
            st.session_state["chat_history"] = []
            clear_chat_history(st.session_state["username"])
            st.success("🧼 History cleared!")
            st.experimental_rerun()

        # Display chat in reverse order (latest first)
        for chat in reversed(chat_history):
            user_text = chat.get("user_msg", "")
            ai_text = chat.get("ai_msg", "")

            # Safe multiline markdown with formatting
            st.markdown(f"""
                <p><strong>🧑 You:</strong> {user_text}</p>
                <p><strong>🤖 AI:</strong> {ai_text}</p>
                <hr>
            """, unsafe_allow_html=True)



elif menu == "Exam":
    st.title("📝 Take an Exam")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        topic = st.text_input("📚 Enter a topic for the exam")
        
        if st.button("🎯 Start Exam") and topic:
            try:
                questions = generate_exam(topic)
                st.session_state["exam_questions"] = questions
                st.session_state["exam_active"] = True
                st.success("✅ Exam started! Answer the questions below.")
            except Exception as e:
                st.error(f"❌ Error generating exam: {str(e)}")

    if st.session_state["exam_active"]:
        st.subheader("📄 Questions")
        
        # Make questions stand out with styled container
        st.markdown(f"""
        <div style="background-color: ""; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
            {st.session_state["exam_questions"]}
        </div>
        """, unsafe_allow_html=True)
        
        answers = st.text_area("✏ Enter your answers (one per line)", key="exam_input", height=200)
        
        if st.button("📤 Submit Answers"):
            try:
                marks, mistakes = evaluate_exam(st.session_state["exam_questions"], answers)
                store_result(st.session_state["username"], topic, marks, mistakes)
                
                # Results with better styling
                st.markdown(f"""
                <div style="background-color: ""; padding: 20px; border-radius: 10px; margin: 20px 0;">
                    <h3>Exam Results</h3>
                    <h4>🎓 Your Score: {marks}/5</h4>
                    <h5>🧠 Feedback:</h5>
                    <div>{mistakes}</div>
                </div>
                """, unsafe_allow_html=True)
                
                st.session_state["exam_active"] = False
            except Exception as e:
                st.error(f"❌ Error evaluating exam: {str(e)}")

elif menu == "Results":
    st.title("📊 Your Results")

    try:
        results = get_user_results(st.session_state["username"])
        if results:
            # Creating a more responsive results display
            for i, result in enumerate(results):
                st.markdown(f"""
                <div style="background-color: {'' if i % 2 == 0 else ''}; 
                            padding: 15px; border-radius: 5px; margin-bottom: 10px; 
                            border-left: 4px solid {'#1976d2' if result['marks'] >= 3 else '#e57373'};">
                    <h4>📌 {result['topic']}</h4>
                    <div style="display: flex; flex-wrap: wrap; gap: 20px;">
                        <div>
                            <strong>🏆 Score:</strong> {result['marks']}/5
                        </div>
                        <div>
                            <strong>🗓 Date:</strong> {result['date']}
                        </div>
                    </div>
                    <div style="margin-top: 10px;">
                        <strong>❗ Feedback:</strong><br>
                        {result['mistakes']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            # Empty state with animation
            col1, col2 = st.columns([2, 3])
            
            with col1:
                st.markdown("""
                <div style="padding: 20px 0;">
                    <h3>No results yet!</h3>
                    <p>Take an exam to see your results here.</p>
                </div>
                """, unsafe_allow_html=True)
                
            with col2:
                lottie_empty = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_ydo1amjm.json")
                if lottie_empty:
                    st_lottie(lottie_empty, height=200, key="empty_results")
                    
    except Exception as e:
        st.error(f"❌ Error fetching results: {str(e)}") 
        
        
        
st.markdown("""
<hr style="border: none; border-top: 2px solid #ccc; margin: 40px 0;" />

<div style="text-align: center; padding: 10px 0;">
    <p style="font-size: 16px; color: gray;">
        © 2025 <strong>GenEDxAI</strong>. All rights reserved.
    </p>
    <p style="font-size: 14px; color: gray;">
        Crafted with <span style="color: #e74c3c;">❤</span> using <strong>Streamlit</strong>. Designed for Lifelong Learners.
    </p>
    <div style="margin-top: 10px;">
        <a href="https://www.linkedin.com" target="_blank" style="margin: 0 10px; text-decoration: none; color: #0e76a8;">LinkedIn</a>
        <a href="https://github.com" target="_blank" style="margin: 0 10px; text-decoration: none; color: #333;">GitHub</a>
        <a href="https://www.facebook.com/" style="margin: 0 10px; text-decoration: none; color: #d44638;">Facebook</a>
    </div>
</div>
""", unsafe_allow_html=True)
