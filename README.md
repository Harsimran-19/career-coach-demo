# Career Coach Agents - Simple Chat UI

A clean, simple chat interface for the Career Coach Agents system built with Streamlit. This UI provides a streamlined chat experience with Sophie, your AI career coach.

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Career Coach Agents API server running

### Installation

1. **Install Dependencies**
   ```bash
   cd ui
   pip install -r requirements.txt
   ```

2. **Start the API Server** (in another terminal)
   ```bash
   cd philoagents-api
   python src/main.py
   ```

3. **Launch the UI**
   ```bash
   # Option 1: Using the startup script (recommended)
   python run_streamlit.py
   
   # Option 2: Direct Streamlit command
   streamlit run streamlit_app.py
   ```

4. **Open Your Browser**
   - Navigate to: http://localhost:8501
   - Start chatting with Sophie, your AI career coach!

## 🎯 Features

### 💬 Simple Chat Interface
- **Native Streamlit Chat**: Clean chat UI with message bubbles
- **Real-time Conversations**: Instant responses from Sophie
- **Message History**: Conversation persists within session
- **User Context**: Add background information for personalized advice

### 👥 Sophie - Your AI Career Coach
Sophie specializes in four areas:
- **🎯 Career Assessment**: MBTI, personality tests, and career exploration
- **📄 Resume Builder**: ATS optimization and resume crafting  
- **💼 LinkedIn Optimizer**: Profile enhancement and personal branding
- **🤝 Networking Strategy**: Professional relationship building strategies

### 🔧 Simple Controls
- **Coach Selection**: Switch between Sophie's specialties
- **Clear Chat**: Reset current conversation
- **Reset Memory**: Clear conversation history from server
- **User Context**: Add your background for better advice

## 📁 Project Structure

```
ui/
├── streamlit_app.py          # Main chat application
├── requirements.txt          # Python dependencies  
├── run_streamlit.py          # Automated startup script
└── README.md                # This file
```

## 💬 Using the Chat Interface

### Starting a Conversation

1. **Select Sophie's Specialty**: Choose from the sidebar dropdown
2. **Add Your Context**: Tell Sophie about your background and situation
3. **Start Chatting**: Type your message and press Enter
4. **Get Personalized Advice**: Sophie will respond based on her specialty

### Sample Questions by Specialty

**🎯 Career Assessment**
- "I'm feeling lost in my career direction. Can you help?"
- "What personality tests can help me understand my career fit?"
- "How do I identify my strengths and interests?"

**📄 Resume Builder**
- "My resume isn't getting me interviews. What's wrong?"
- "How do I optimize my resume for ATS systems?"
- "Can you help me write a cover letter?"

**💼 LinkedIn Optimizer**
- "How do I create a LinkedIn headline that stands out?"
- "What should I include in my LinkedIn summary?"
- "How can I make my profile more visible to recruiters?"

**🤝 Networking Strategy**
- "I'm an introvert. How can I network effectively?"
- "What's the best way to reach out to people on LinkedIn?"
- "How do I build professional relationships?"

## 🔧 Troubleshooting

### Common Issues

#### API Connection Failed
```
❌ Cannot connect to API server
```
**Solution**:
1. Ensure the API server is running: `python src/main.py`
2. Check that the server is accessible at http://localhost:8000
3. Verify no firewall is blocking the connection

#### Coach Not Responding
```
Failed to get response from coach
```
**Solution**:
1. Check API server logs for errors
2. Verify your API keys are configured in `.env`
3. Try resetting the conversation memory

#### Streamlit App Won't Start
```
ModuleNotFoundError: No module named 'streamlit'
```
**Solution**:
1. Install dependencies: `pip install -r requirements.txt`
2. Use Python 3.8 or higher
3. Consider using a virtual environment

## 🚀 Development

### Customization

- **Styling**: The app uses Streamlit's default styling for simplicity
- **Coaches**: Add new specialties by updating the `COACHES` dictionary
- **API Integration**: Modify the `send_message()` function for different endpoints

### Adding Features

1. **New Coach Specialties**: Update the `COACHES` dictionary in `streamlit_app.py`
2. **Enhanced UI**: Add more Streamlit components as needed
3. **Additional Controls**: Extend the sidebar with new functionality

## 📄 License

Same license as the parent Career Coach Agents project.

---

**Happy Coaching! 🎯**

For more information about the Career Coach Agents system, see the main project documentation.
