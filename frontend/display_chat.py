import streamlit as st


def display_chat_messages(chat_history):
    """Display chat messages using Streamlit's chat components"""
    for message in chat_history:
        # Display user messages with user avatar
        if message['role'] == 'user':
            with st.chat_message("user", avatar="👤"):
                st.write(message['content'])
        # Display assistant messages with assistant avatar
        else:
            with st.chat_message("assistant", avatar="🤖"):
                st.write(message['content'])
