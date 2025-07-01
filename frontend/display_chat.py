import streamlit as st


def display_chat_messages(chat_history):
    """Display chat messages using Streamlit's chat components"""
    for message in chat_history:
        if message['role'] == 'user':
            with st.chat_message("user", avatar="👤"):
                st.write(message['content'])
        else:
            with st.chat_message("assistant", avatar="🤖"):
                st.write(message['content'])
