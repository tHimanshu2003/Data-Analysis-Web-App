import streamlit as st
from dependancies import sign_up
from main import re_direct


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

st.sidebar.title("Get Back to Home!")
Home_Button = st.sidebar.button("<<< Back to Home", key="b1")
if Home_Button:
    re_direct("http://127.0.0.1:5000")
st.sidebar.title("Get Back to Login!")
login = st.sidebar.button("<<< Back to Login", key="b2")
if login:
    re_direct("http://localhost:8501")

sign_up()
