import streamlit as st
import requests
import os
import sys
from display_chat import display_chat_messages

# append the path of the parent directory
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
    os.environ["GEMINI_API_KEY"] = api_key
    user_input = st.chat_input("Type your message here...")
    history = st.session_state["messages"]
    if user_input:
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
                agent_reply = agent_reply.get("detail")
        except Exception as e:
            agent_reply = f"[Error: {e}]"
        message = {"role": "assistant", "content": agent_reply.get("response")}
        st.session_state.messages.append(message)
    display_chat_messages(history)


if gemini_api_key:
    current_chat(gemini_api_key)
else:
    st.warning("Please enter your Gemini API key!", icon="⚠")
