import streamlit as st
import os

st.set_page_config(page_title="Get To Know Me", page_icon="ℹ️", layout="centered")

st.header("ℹ️ Get to Know Me")
st.subheader("Matthew — Instructor Background")

# Picture layout split
col1, col2 = st.columns(2)
with col1:
    image_path = "pictures/profile.jpg" 
    if os.path.exists(image_path):
        st.image(image_path, width="stretch")
    else:
        st.info("📷 Profile picture placeholder")

with col2:
    st.markdown("""
    Welcome! My professional field centers directly on **STEM** (Science, Technology, Engineering, and Math). 
    I believe that the best way to understand how the world works is to take things apart and build models of them.
    """)

st.markdown("""
Merging a background in physical sciences with computer systems shapes my unique technical approach. 
I aim to show K-5 students that math and coding aren't just rows of numbers on a screen—they are the 
underlying building blocks used to construct video games, spaceships, and clever engineering projects.
""")

with st.container(border=True):
    st.markdown("### 🎯 Educational Philosophy")
    st.write("I focus heavily on project-based learning. By turning advanced logic frameworks into playable, interactive labs, kids learn to naturally break down complex problems into small, manageable milestones.")
