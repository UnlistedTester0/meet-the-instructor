import streamlit as st
import os

st.set_page_config(page_title="Get To Know Me", page_icon="ℹ️", layout="centered")

st.header("ℹ️ Get to Know Me")
st.subheader("Matthew — Instructor Background")

# Top Layout Split: Photo & Intro Bio Text
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

# Educational Philosophy Container Card
with st.container(border=True):
    st.markdown("### 🎯 Educational Philosophy")
    st.write("I focus heavily on project-based learning. By turning advanced logic frameworks into playable, interactive labs, kids learn to naturally break down complex problems into small, manageable milestones.")

# --- NEW VISUAL ASSET CONTAINER ZONE ---
# Positioned cleanly at the base of your text profile profile layout
extra_img_path = "pictures/UnlistedPlatform0.jpg"  # Change extension to .png if necessary

with st.container(border=True):
    if os.path.exists(extra_img_path):
        st.image(extra_img_path, caption="🛡️ My Unlisted BattleStation 🛡️", width="stretch")
    else:
        st.info("📷 [Pictures Folder] UnlistedPlatform0 Asset Placeholder")
        
# --- NEW ADORABLE VISUAL CONTAINER ---
# Positioned at the absolute bottom of your personal background chapter
cat_img_path = "pictures/CatPC.jpg"  # Adjust to .png in Notepad++ if your file uses it!

with st.container(border=True):
    if os.path.exists(cat_img_path):
        st.image(cat_img_path, caption="🐈 Cats and Computers: A Timeless Classic", width="stretch")
    else:
        st.info("📷 [Pictures Folder] CatPC.jpg Asset Placeholder")