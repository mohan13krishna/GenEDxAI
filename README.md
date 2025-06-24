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

## 🌟 Meet Our Legendary Team

<div align="center">

### ⚡ **The Visionary Architects of GenEDxAI** ⚡

*Where Innovation Meets Excellence*

</div>

---

<div align="center">

```
                          🌟 TEAM CONSTELLATION 🌟
                                    
                            🎨 Uday Kiran Neelam
                          ╭─────────────────────╮
                      🤖 ─┤    FRONTEND WIZARD   ├─ 🗄️
                Rakesh     ╰─────────────────────╯     Ranjith
               Kolipaka              │                 Kumar
                  │                 │                 Digutla
                  │           ⚙️ Mohan Krishna        │
                  │            Thalla (CORE)          │
                  │                 │                 │
          ╭───────────────╮         │         ╭──────────────╮
          │  AI MASTERMIND │    ━━━━━┷━━━━━    │ DATA SORCERER│
          ╰───────────────╯                  ╰──────────────╯
                                    
               💡 Innovation Hub 💡
```

</div>

---

<div align="center">

### 🎭 **The Fantastic Four** 🎭

</div>

<table align="center">
<tr>
<td align="center" width="50%" style="padding: 20px;">

```
    ╔══════════════════════════════════╗
    ║         🎨 FRONTEND WIZARD        ║
    ╠══════════════════════════════════╣
    ║                                  ║
```
<img src="https://github.com/udaykiran2102.png" width="100px" style="border-radius: 50%; border: 5px solid #00d4ff; box-shadow: 0 0 30px #00d4ff, inset 0 0 10px rgba(0,212,255,0.3);"/>

**[Uday Kiran Neelam](https://github.com/udaykiran2102)**

```
    ║  ✨ UI/UX Design Mastery         ║
    ║  🎯 React Development Expert     ║
    ║  🌈 User Experience Architect    ║
    ║                                  ║
    ║  "Crafting digital poetry        ║
    ║   that users fall in love with"  ║
    ╚══════════════════════════════════╝
```

</td>
<td align="center" width="50%" style="padding: 20px;">

```
    ╔══════════════════════════════════╗
    ║        ⚙️ BACKEND ARCHITECT       ║
    ╠══════════════════════════════════╣
    ║                                  ║
```
<img src="https://github.com/mohan13krishna.png" width="100px" style="border-radius: 50%; border: 5px solid #ff6b6b; box-shadow: 0 0 30px #ff6b6b, inset 0 0 10px rgba(255,107,107,0.3);"/>

**[Mohan Krishna Thalla](https://github.com/mohan13krishna)**

```
    ║  🏗️ Server Architecture Genius   ║
    ║  🔌 API Development Specialist   ║
    ║  🎯 System Design Virtuoso       ║
    ║                                  ║
    ║  "Building the invisible         ║
    ║   foundation of tomorrow"        ║
    ╚══════════════════════════════════╝
```

</td>
</tr>
<tr>
<td align="center" width="50%" style="padding: 20px;">

```
    ╔══════════════════════════════════╗
    ║         🤖 AI MASTERMIND          ║
    ╠══════════════════════════════════╣
    ║                                  ║
```
<img src="https://github.com/rakeshkolipakaace.png" width="100px" style="border-radius: 50%; border: 5px solid #4ecdc4; box-shadow: 0 0 30px #4ecdc4, inset 0 0 10px rgba(78,205,196,0.3);"/>

**[Rakesh Kolipaka](https://github.com/rakeshkolipakaace)**

```
    ║  🧠 Machine Learning Sage        ║
    ║  🔮 Gemini AI Integration Pro    ║
    ║  ⚡ Smart Algorithm Designer     ║
    ║                                  ║
    ║  "Teaching silicon minds         ║
    ║   to understand human hearts"    ║
    ╚══════════════════════════════════╝
```

</td>
<td align="center" width="50%" style="padding: 20px;">

```
    ╔══════════════════════════════════╗
    ║         🗄️ DATA SORCERER          ║
    ╠══════════════════════════════════╣
    ║                                  ║
```
<img src="https://github.com/ranjith93250.png" width="100px" style="border-radius: 50%; border: 5px solid #95e1d3; box-shadow: 0 0 30px #95e1d3, inset 0 0 10px rgba(149,225,211,0.3);"/>

**[Ranjith Kumar Digutla](https://github.com/ranjith93250)**

```
    ║  📊 Database Design Architect    ║
    ║  🛡️ MongoDB Security Guardian    ║
    ║  🌊 Data Flow Orchestrator       ║
    ║                                  ║
    ║  "Weaving data symphonies        ║
    ║   that power digital dreams"     ║
    ╚══════════════════════════════════╝
```

</td>
</tr>
</table>

---

<div align="center">

### 🎆 **The Sacred Geometry of Success** 🎆

```
                    🌟 VISION 🌟
                         │
                    ┌────┴────┐
                    │ PASSION │
               ┌────┴────┐    └────┬────┐
               │ SKILL   │         │ TEAMWORK │
          ┌────┴────┐    └────┬────┘    └────┬────┐
          │ CODE    │         │ AI │         │ DATA │
          └─────────┘    ┌────┴────┐    ┌────┴─────┐
                         │ DESIGN  │    │ INNOVATION│
                         └─────────┘    └───────────┘
                              │              │
                         ╔════════════════════════╗
                         ║      🚀 GENEDXAI       ║
                         ║   Future of Learning   ║
                         ╚════════════════════════╝
```

</div>

---

<div align="center">

### 💫 **Our Magical Formula** 💫

```
┌─────────────────────────────────────────────────────────────┐
│  🎨 CREATIVITY × ⚙️ ENGINEERING × 🤖 INTELLIGENCE × 🗄️ WISDOM  │
│                              ║                              │
│                         ═══════════                        │
│                              ▼                              │
│                     ✨ EDUCATIONAL MAGIC ✨                │
└─────────────────────────────────────────────────────────────┘
```

**Mission Decoder:** *"Transforming curiosity into knowledge, one AI interaction at a time"*

**Vision Amplifier:** *"Building bridges between human potential and artificial intelligence"*

</div>

---

<div align="center">

### 🌈 **The DNA of GenEDxAI** 🌈

```
        🧬 Innovation Helix 🧬
           
    A ═══╗     ╔═══ T     
        ║     ║         
    G ═══╝     ╚═══ C     
        
    A = 🎨 Artistry (Frontend Magic)
    T = 🔧 Technology (Backend Power) 
    G = 🧠 Genius (AI Intelligence)
    C = 📊 Computation (Data Mastery)
```

*The perfect genetic combination for educational evolution!* 🚀

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
