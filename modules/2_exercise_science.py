import streamlit as st

st.set_page_config(page_title="Exercise Science", page_icon="🏃‍♂️", layout="centered")

st.header("🏃‍♂️ Exercise Science Background")
st.subheader("Black Hills State University — Spearfish, SD")

st.markdown("""
Before diving deeply into digital computing systems, I completed **3 years of undergraduate study in Exercise Science** 
at Black Hills State University. 

Studying how living systems move, adapt, and process energy directly shapes how I approach software design 
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
