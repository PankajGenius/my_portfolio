import streamlit as st
import pandas


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/pankaj.jpg" )

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

info = """
Below you can find some of the apps. I have build in python. Feel free to contact me 
"""
st.write(info)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

