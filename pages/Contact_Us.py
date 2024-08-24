import streamlit as st
from semd_email import email_sending
st.header("Contact Me ")

with st.form(key="Your email"):
    user_email = st.text_input("Enter your email address")
    message = st.text_area("Your message")
    message = f"""\
Subject : New email from {user_email}
 
From : {user_email}
{message} 
"""
    button = st.form_submit_button("Submit")

    if button:
        email_sending(message)
        st.info("Message sent successfully")
