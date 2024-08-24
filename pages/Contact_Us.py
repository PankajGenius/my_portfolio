import streamlit as st
st.header("Contact Me ")

with st.form(key="Your email"):
    user_email = st.text_input("Enter your email address")
    email = st.text_area("Your message")
    button = st.form_submit_button("Submit")

    if button:
        print("Successfully submitted")