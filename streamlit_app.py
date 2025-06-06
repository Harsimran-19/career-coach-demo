import streamlit as st
import requests
import uuid
from typing import Dict, Optional

# Page configuration
st.set_page_config(
    page_title="Career Coach Agents",
    page_icon="🎯",
    layout="centered"
)

# Configuration
API_BASE_URL = "https://uapcfqiypm.us-east-1.awsapprunner.com"
CAREER_COACHES_API = f"{API_BASE_URL}/career-coach"

# Available coaches
COACHES = {
    "career_assessment": {
        "name": "Sophie - Career Assessment",
        "description": "Career assessment and path planning specialist",
        "emoji": "🎯"
    },
    "resume_builder": {
        "name": "Sophie - Resume Builder", 
        "description": "Resume writing and ATS optimization expert",
        "emoji": "📄"
    },
    "linkedin_optimizer": {
        "name": "Sophie - LinkedIn Optimizer",
        "description": "LinkedIn profile and personal branding specialist", 
        "emoji": "💼"
    },
    "networking_strategy": {
        "name": "Sophie - Networking Strategy",
        "description": "Professional networking and relationship building coach",
        "emoji": "🤝"
    }
}

def initialize_session_state():
    """Initialize session state variables."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "user_id" not in st.session_state:
        st.session_state.user_id = f"user_{str(uuid.uuid4())[:8]}"
    if "selected_coach" not in st.session_state:
        st.session_state.selected_coach = "career_assessment"

def send_message(message: str, coach_id: str, user_id: str, user_context: str = "") -> Optional[str]:
    """Send a message to the career coach API."""
    try:
        payload = {
            "message": message,
            "coach_id": coach_id,
            "user_id": user_id,
            "user_context": user_context,
            "session_goals": []
        }

        response = requests.post(
            f"{CAREER_COACHES_API}/chat",
            json=payload,
            timeout=30
        )

        if response.status_code == 200:
            result = response.json()
            return result.get("response", "No response received")
        else:
            st.error(f"API Error: {response.status_code}")
            return None

    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to API server. Please ensure the API server is running.")
        st.info("Start the API server with: `python src/main.py` in the philoagents-api directory")
        return None
    except requests.exceptions.Timeout:
        st.error("⏰ Request timed out. The API server might be overloaded.")
        return None
    except requests.exceptions.RequestException as e:
        st.error(f"🔌 Connection error: {e}")
        return None

def reset_conversation(user_id: str) -> bool:
    """Reset the conversation memory for a user."""
    try:
        payload = {"user_id": user_id}
        response = requests.post(
            f"{CAREER_COACHES_API}/reset-memory",
            json=payload,
            timeout=10
        )
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def main():
    """Main application."""
    initialize_session_state()
    
    # Header
    st.title("🎯 Career Coach Agents")
    st.markdown("Get personalized career guidance from AI specialists")
    
    # Sidebar for coach selection and settings
    with st.sidebar:
        st.header("🔧 Settings")
        
        # Coach selection
        st.subheader("👥 Select Coach")
        coach_options = {f"{coach['emoji']} {coach['name']}": coach_id 
                        for coach_id, coach in COACHES.items()}
        
        selected_coach_display = st.selectbox(
            "Choose your career coach:",
            options=list(coach_options.keys()),
            index=0
        )
        
        st.session_state.selected_coach = coach_options[selected_coach_display]
        
        # Show coach description
        coach_info = COACHES[st.session_state.selected_coach]
        st.info(f"**{coach_info['name']}**\n\n{coach_info['description']}")
        
        # User context
        st.subheader("📝 Your Context")
        user_context = st.text_area(
            "Tell us about your situation:",
            placeholder="e.g., Recent graduate, 5 years experience in marketing, looking for career change...",
            height=100
        )
        
        # Controls
        st.subheader("🎮 Controls")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🗑️ Clear Chat"):
                st.session_state.messages = []
                st.rerun()
        
        with col2:
            if st.button("🔄 Reset Memory"):
                if reset_conversation(st.session_state.user_id):
                    st.success("Memory reset!")
                    st.session_state.messages = []
                    st.rerun()
                else:
                    st.error("Failed to reset memory")
        
        # User ID display
        st.markdown("---")
        st.caption(f"User ID: {st.session_state.user_id}")
    
    # Main chat interface
    st.markdown("---")
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get coach response
        with st.chat_message("assistant"):
            with st.spinner("Sophie is thinking..."):
                response = send_message(
                    message=prompt,
                    coach_id=st.session_state.selected_coach,
                    user_id=st.session_state.user_id,
                    user_context=user_context
                )
            
            if response:
                st.markdown(response)
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})
            else:
                st.error("Failed to get response from coach. Please try again.")

if __name__ == "__main__":
    main()
