import streamlit as st
import requests
import os
import sys
from display_chat import display_chat_messages

# Add parent directory to sys.path for imports
sys.path.append("..")
from shared import constants

st.title("🏠 Real Estate Asset Assistant")

# Sidebar for API Key
st.sidebar.title("API Key")
gemini_api_key = st.sidebar.text_input("Gemini API Key", type="password")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How may I assist you today?"}]


def current_chat(api_key):
    """Displays the active chat interface with message history and input functionality."""
    os.environ["GEMINI_API_KEY"] = api_key
    user_input = st.chat_input("Type your message here...")
    history = st.session_state["messages"]
    if user_input:
        # Append user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        message_history = [msg["content"] for msg in history]
        # Call FastAPI backend
        try:
            response = requests.post(f"{constants.API_URL}/chat/",
                                     json={"api_key": api_key,
                                           "content": message_history,
                                           "config": {
                                               "temperature": constants.DEFAULT_TEMPERATURE,
                                               "max_output_tokens": constants.MAX_TOKENS
                                           },
                                           }
                                     )
            agent_reply = response.json()
            if response.status_code != 200:
                st.error(f"Failed to send message: {agent_reply.get('detail')}")

            # Append assistant's reply to chat history
            message = {"role": "assistant", "content": agent_reply.get("response")}
            st.session_state.messages.append(message)
        except Exception as e:
            st.error(f"Failed to send message: {e}")
    # Display the chat messages
    display_chat_messages(history)


# Run chat if API key is provided
if gemini_api_key:
    current_chat(gemini_api_key)
else:
    st.warning("Please enter your Gemini API key!", icon="⚠")
