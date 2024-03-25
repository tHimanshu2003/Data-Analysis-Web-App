import streamlit as st
from dependancies import sign_up
from main import re_direct


st.set_page_config(
    page_title="Data Mind",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Report a bug": "http://127.0.0.1:5000/feedback",
        "About": "# This is a header. This is an *extremely* cool app!",
    },
)

st.markdown(
    """
    <style>
    .stDeployButton {
            visibility: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title("Get Back to Home")
home_button = st.sidebar.button("🏠 Home", key="home")
if home_button:
    re_direct("http://127.0.0.1:5000")
st.sidebar.title("Want to Login?")
login = st.sidebar.button("🔑 Login")
if login:
    re_direct("http://localhost:8501")

sign_up()
