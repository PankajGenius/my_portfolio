import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width= 200 )

with col2:
    st.title("Pankaj")
    content = """
    Hii I am Pankaj! I have completed my graduation in Bachelor of Computer Application(BCA) 
    from Delhi Skills and Entrepreneurship University. I have a good Knowledge in Python Programming 
    as well as I have done a project in it. Currently, I am looking for a job. 
    As I am a fresher I am eager to learn new things and with my problem solving abilities. 
    I am confident that I can make meaningful contribution at your organisation. 
    """
    st.info(content)