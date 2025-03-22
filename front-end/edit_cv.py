import os
import random
import time
import streamlit as st

st.set_page_config(layout="wide")

def load_index_page():
    cv_path = os.path.join(os.path.dirname(__file__), "..", "output", "cv.html")
    with open(cv_path, 'r', encoding='utf-8') as f:
        cv_content = f.read()
    return cv_content

# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

def display_edit_cv_page():

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            if message["role"] == "assistant":
                st.html(message["content"])
            else:
                st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response = load_index_page()
            st.html(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

display_edit_cv_page()