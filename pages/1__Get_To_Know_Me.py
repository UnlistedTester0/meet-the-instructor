import streamlit as st
import os

st.set_page_config(page_title="Get To Know Me", page_icon="ℹ️", layout="centered")

st.header("ℹ️ Get to Know Me")
st.subheader("Matthew — Instructor Background")

# Create a side-by-side split layout for your photo and text profile
col1, col2 = st.columns(2)

with col1:
    # Points inside your central pictures folder
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

st.markdown("---")
st.subheader("📂 Explore My Specialties & Resources")

# ROW 1: Academic Focus Areas
nav_row1_col1, nav_row1_col2 = st.columns(2)
with nav_row1_col1:
    if st.button("🏃‍♂️ Exercise Science Study", use_container_width=True):
        st.switch_page("pages/2_Exercise_Science.py")
with nav_row1_col2:
    if st.button("💻 Computer Science Skills", use_container_width=True):
        st.switch_page("pages/3_Computer_Science.py")

nav_row2_col1, nav_row2_col2, nav_row2_col3 = st.columns(3)
with nav_row2_col1:
    if st.button("🧗 Rock Climbing", use_container_width=True):
        st.switch_page("pages/4_Rock_Climbing.py")
with nav_row2_col2:
    if st.button("🥗 Sports Nutrition", use_container_width=True):
        st.switch_page("pages/5_Nutrition.py")
with nav_row2_col3:
    if st.button("📋 Learning Plan", use_container_width=True):
        st.switch_page("pages/6_Learning_Plan.py")

st.markdown("---")

# ROW 3: App Return Vector Direction (Moved completely to the bottom!)
if st.button("⬅️ Back to Main Menu", use_container_width=True):
    st.switch_page("app.py")
