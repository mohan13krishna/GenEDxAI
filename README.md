# GenEDxAI: AI-Powered Chatbot for Education    
            
#### A new way of GenZ learning with AI Powered Chatbot           
                                              
## 🔗 Live Demo                                                                        
**[Try GenEDxAI Now](https://genedxai.onrender.com)**                                                                                  
                                                                          
## 🤖 Overview                                        
            
GenEDxAI is an innovative AI-powered education platform designed for GenZ learners. It combines interactive learning with personalized assessments to create a dynamic educational experience. The platform leverages Google's Gemini AI to provide intelligent responses to learning queries and generate customized exams.  
   
           
## ✨ Features          
    
- **🧠 Interactive Learning:** Ask questions on any topic and get detailed, educational responses 
- **📝 Personalized Exams:** Generate custom exams on any subject with automatic evaluation 
- **📊 Progress Tracking:** Monitor your learning journey with comprehensive result history
- **🔐 Secure User Management:** Personal accounts with secure authentication
- **📱 Responsive Design:** Optimized for both desktop and mobile devices

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- MongoDB (local or cloud instance)
- Google Gemini API key

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/mohan13krishna/GenEDxAI
cd genedxai
```

2. **Create and activate a virtual environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure your environment**

Create a new file under `config/config.py` with the following content:

```python
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"  # Replace with your actual Gemini API key
MONGODB_URI = "mongodb://localhost:27017/"  # Update with your MongoDB connection string if using cloud
DB_NAME = "edu_chatbot"
```

> ⚠️ **IMPORTANT**: Replace `YOUR_GEMINI_API_KEY` with your actual Google Gemini API key.

5. **Run the application**

```bash
streamlit run app.py
```

## 🏗️ Project Structure

```
GenEDxAI/
├── 📁 .devcontainer/
│   └── 📄 devcontainer.json
├── 📁 config/
│   ├── 📁 __pycache__/
│   ├── 🐍 __init__.py
│   └── ⚙️ config.py                  # Configuration file with API keys and database settings
├── 📁 static/
│   ├── 📁 videos/                    # Video assets for UI
│   ├── 🎨 ai.json                    # Configuration for AI animations
│   └── 🎨 style.css                  # Custom CSS for styling the application
├── 📁 utils/
│   ├── 📁 __pycache__/
│   ├── 🐍 __init__.py                # Utils package initialization
│   ├── 🔐 auth.py                    # User authentication functionality
│   ├── 🤖 chatbot.py                 # Core chatbot functionality using Gemini AI
│   ├── 🗄️ db.py                      # Database operations and MongoDB connections
│   └── 📝 exam.py                    # Exam generation and evaluation logic
├── 📁 venv/                          # Virtual environment folder
│   ├── 📁 Include/
│   ├── 📁 Lib/
│   ├── 📁 Scripts/
│   ├── 📁 share/
│   └── ⚙️ pyvenv.cfg
├── 🚀 app.py                         # Main application entry point (Streamlit app)
├── 🌍 .env                           # Environment variables (keep this secure!)
├── 🔧 .gitignore                     # Git ignore rules
├── 📚 README.md                      # Project documentation
└── 📋 requirements.txt               # Project dependencies
```

## 🔧 Configuration

### MongoDB Setup

1. Install MongoDB locally or use a cloud service like MongoDB Atlas
2. Update the `MONGODB_URI` in `config.py` with your connection string
3. The application will automatically create the required collections

### Gemini API Key

1. Visit the [Google AI Studio](https://ai.google.dev/) to get your API key
2. Set the `GEMINI_API_KEY` in `config.py`

## 📚 Usage

### Registration & Login

1. Launch the application and navigate to the "Register" tab
2. Create a new account with a username and password
3. Return to the "Login" tab and sign in with your credentials

### Learning Mode

1. Navigate to the "Learn" tab
2. Type your question or topic in the text area
3. Click "Submit" to receive an educational response from the AI

### Exam Mode

1. Navigate to the "Exam" tab
2. Enter a topic for your exam
3. Click "Start Exam" to generate a customized 5-question quiz
4. Answer each question and submit for automatic evaluation

### Results Tracking

1. Navigate to the "Results" tab to view your exam history
2. Review your scores, topics, and feedback for improvement

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👏 Acknowledgements

- [Streamlit](https://streamlit.io/) for the wonderful web framework
- [Google Gemini AI](https://ai.google.dev/) for powering our learning responses
- [MongoDB](https://www.mongodb.com/) for database solutions
- [Lottie Files](https://lottiefiles.com/) for beautiful animations

## 🌟 Meet Our Amazing Team

<div align="center">

### 💫 **The Brilliant Minds Behind GenEDxAI** 💫

</div>

---

<div align="center">

<table>
<tr>
<td align="center" width="250px">
<div style="background: linear-gradient(145deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); margin: 15px;">
<img src="https://github.com/udaykiran2102.png" width="120px" style="border-radius: 50%; border: 4px solid white; margin-bottom: 15px;"/>
<h3 style="color: white; margin: 10px 0;">🎨 Frontend Developer</h3>
<h2 style="color: white; margin: 5px 0;"><a href="https://github.com/udaykiran2102" style="color: white; text-decoration: none;">Uday Kiran Neelam</a></h2>
<p style="color: #f0f0f0; font-style: italic; margin: 10px 0;">"Crafting beautiful user experiences"</p>
</div>
</td>
<td align="center" width="250px">
<div style="background: linear-gradient(145deg, #f093fb 0%, #f5576c 100%); padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); margin: 15px;">
<img src="https://github.com/mohan13krishna.png" width="120px" style="border-radius: 50%; border: 4px solid white; margin-bottom: 15px;"/>
<h3 style="color: white; margin: 10px 0;">⚙️ Backend Developer</h3>
<h2 style="color: white; margin: 5px 0;"><a href="https://github.com/mohan13krishna" style="color: white; text-decoration: none;">Mohan Krishna Thalla</a></h2>
<p style="color: #f0f0f0; font-style: italic; margin: 10px 0;">"Building robust server architecture"</p>
</div>
</td>
</tr>
<tr>
<td align="center" width="250px">
<div style="background: linear-gradient(145deg, #4facfe 0%, #00f2fe 100%); padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); margin: 15px;">
<img src="https://github.com/rakeshkolipakaace.png" width="120px" style="border-radius: 50%; border: 4px solid white; margin-bottom: 15px;"/>
<h3 style="color: white; margin: 10px 0;">🤖 AI Integration Engineer</h3>
<h2 style="color: white; margin: 5px 0;"><a href="https://github.com/rakeshkolipakaace" style="color: white; text-decoration: none;">Rakesh Kolipaka</a></h2>
<p style="color: #f0f0f0; font-style: italic; margin: 10px 0;">"Integrating intelligent AI solutions"</p>
</div>
</td>
<td align="center" width="250px">
<div style="background: linear-gradient(145deg, #a8edea 0%, #fed6e3 100%); padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); margin: 15px;">
<img src="https://github.com/ranjith93250.png" width="120px" style="border-radius: 50%; border: 4px solid white; margin-bottom: 15px;"/>
<h3 style="color: #333; margin: 10px 0;">🗄️ Database Manager</h3>
<h2 style="color: #333; margin: 5px 0;"><a href="https://github.com/ranjith93250" style="color: #333; text-decoration: none;">Ranjith Kumar Digutla</a></h2>
<p style="color: #555; font-style: italic; margin: 10px 0;">"Managing data architecture"</p>
</div>
</td>
</tr>
</table>

</div>

---

<div align="center">

### 🚀 **Our Mission** 
*"Revolutionizing education through AI-powered learning experiences for the next generation"*

### 🎯 **Our Vision**
*"Making quality education accessible, interactive, and personalized for every GenZ learner"*

</div>

---

## 📞 Contact

**Project Repository:** [https://github.com/mohan13krishna/GenEDxAI](https://github.com/mohan13krishna/GenEDxAI)

**Live Demo:** [https://genedxai.onrender.com](https://genedxai.onrender.com)

---

<div align="center">

⭐ **Star this repository if you find it helpful!** ⭐

*Built with ❤️ by the GenEDxAI Team*

</div>

---

> **Note**: This project is for educational purposes. Please use responsibly and respect the terms of service of all integrated APIs.
