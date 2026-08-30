import streamlit as st
import os

st.set_page_config(page_title="Exercise Science", page_icon="🏃‍♂️", layout="centered")

st.header("🏃‍♂️ Exercise Science Background")
st.subheader("Black Hills State University — Spearfish, SD")

st.markdown("""
Before diving deeply into digital computing systems, I completed **3 years of undergraduate study in Exercise Science** 
at Black Hills State University. 

What I learned about how living systems move, adapt, and process energy directly shapes how I approach software design 
and systems engineering today:
""")

with st.container(border=True):
    st.markdown("#### 🦴 Biomechanics & Kinesiology")
    st.write("""
    Analyzing physical forces, lever distributions, and movement mechanics taught me how to translate 
    real-world physics interactions into clean software math. This background makes programming physical simulation 
    boundaries or fluid movements instinctive.
    """)

with st.container(border=True):
    st.markdown("#### 🔬 Complex Biological Loops")
    st.write("""
    Human biology is filled with intricate feedback loops and automated balances. Studying these organic 
    frameworks sparked my passion for building custom computer simulations, leading directly into my interest 
    in modeling complex systems, artificial life (ALife) engines, and physics kernels.
    """)

# --- NEW VISUAL ASSET CONTAINER ZONE ---
# Positioned at the bottom of the page to showcase athletic endurance application
mudder_img_path = "pictures/ToughMudder.jpg"

with st.container(border=True):
    if os.path.exists(mudder_img_path):
        st.image(mudder_img_path, caption="🏅 Putting Exercise Science to the Test: Tough Mudder Finish", width="stretch")
    else:
        st.info("📷 [Pictures Folder] ToughMudder.jpg Asset Placeholder")
