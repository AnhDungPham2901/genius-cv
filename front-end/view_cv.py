import os
import streamlit as st

st.set_page_config(layout="wide")

def load_index_page():
    cv_path = os.path.join(os.path.dirname(__file__), "..", "output", "cv.html")
    with open(cv_path, 'r', encoding='utf-8') as f:
        cv_content = f.read()
    return cv_content


st.link_button("Open CV", "https://oigpt.s3.us-east-1.amazonaws.com/cv.html")