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

<table align="center">
<tr>
<td align="center" width="25%">
<img src="https://github.com/udaykiran2102.png" width="120px" style="border-radius: 50%; border: 3px solid #00d4ff;"/><br/>
<b>🎨 Frontend Developer</b><br/>
<h3><a href="https://github.com/udaykiran2102">Uday Kiran Neelam</a></h3>
<sub>Crafting Beautiful User Experiences</sub><br/>
<em>"Making AI accessible through stunning interfaces"</em>
</td>
<td align="center" width="25%">
<img src="https://github.com/mohan13krishna.png" width="120px" style="border-radius: 50%; border: 3px solid #ff6b6b;"/><br/>
<b>⚙️ Backend Developer</b><br/>
<h3><a href="https://github.com/mohan13krishna">Mohan Krishna Thalla</a></h3>
<sub>Building Robust Server Architecture</sub><br/>
<em>"Powering seamless learning experiences"</em>
</td>
</tr>
<tr>
<td align="center" width="25%">
<img src="https://github.com/rakeshkolipakaace.png" width="120px" style="border-radius: 50%; border: 3px solid #4ecdc4;"/><br/>
<b>🤖 AI Integration Engineer</b><br/>
<h3><a href="https://github.com/rakeshkolipakaace">Rakesh Kolipaka</a></h3>
<sub>Integrating Intelligent Solutions</sub><br/>
<em>"Bridging human curiosity with AI wisdom"</em>
</td>
<td align="center" width="25%">
<img src="https://github.com/ranjith93250.png" width="120px" style="border-radius: 50%; border: 3px solid #95e1d3;"/><br/>
<b>🗄️ Database Manager</b><br/>
<h3><a href="https://github.com/ranjith93250">Ranjith Kumar Digutla</a></h3>
<sub>Managing Data Architecture</sub><br/>
<em>"Ensuring data flows like poetry"</em>
</td>
</tr>
</table>

---

<div align="center">

### 🚀 **Our Mission** 
*"Revolutionizing education through AI-powered learning experiences for the next generation"*

### 🎯 **Our Vision**
*"Making quality education accessible, interactive, and personalized for every GenZ learner"*

</div>

---

## 👨‍🏫 Faculty Guidance

<div align="center">

### 🎓 **Under the Guidance of Our Esteemed Faculty Coordinators** 🎓

</div>

---

<table align="center">
<tr>
<td align="center" width="33%">
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 15px; margin: 10px;">
<h3>👩‍🏫 Mrs. P. Swaroopa</h3>
<b>Subject Faculty Coordinator</b><br/>
<sub>Guiding Academic Excellence</sub><br/>
<em>"Inspiring innovation in education technology"</em>
</div>
</td>
<td align="center" width="33%">
<div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 20px; border-radius: 15px; margin: 10px;">
<h3>👨‍🏫 Dr. M. V. Vijaya Saradhi</h3>
<b>Subject Faculty Coordinator</b><br/>
<sub>Research & Development Mentor</sub><br/>
<em>"Fostering cutting-edge AI research"</em>
</div>
</td>
<td align="center" width="33%">
<div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 20px; border-radius: 15px; margin: 10px;">
<h3>👩‍🏫 Mrs. Ch. Srivasta</h3>
<b>Subject Faculty Coordinator</b><br/>
<sub>Technical Excellence Guide</sub><br/>
<em>"Shaping tomorrow's tech leaders"</em>
</div>
</td>
</tr>
</table>

---

<div align="center">

### 🙏 **Acknowledgment**
*"We extend our heartfelt gratitude to our faculty coordinators for their invaluable guidance, mentorship, and continuous support throughout this project. Their expertise and encouragement have been instrumental in bringing GenEDxAI to life."*

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
