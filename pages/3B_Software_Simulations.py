import streamlit as st

st.set_page_config(page_title="Software Simulations", page_icon="💾", layout="centered")

st.header("💾 Software Engineering & Simulations")
st.subheader("Custom Code Engines & Physical Systems modeling")

st.markdown("""
Writing code isn't just about outputting data—it's about building virtual worlds. I create standalone engines 
and math environments to study complex physical interactions.
""")

with st.container(border=True):
    st.markdown("#### ⚙️ Low-Level Programming Languages")
    st.write("I develop cross-platform systems and custom logic matrices utilizing highly efficient development languages like **Python and C++**.")

with st.container(border=True):
    st.markdown("#### 🧬 Custom Physics & ALife Systems")
    st.write("I design algorithms that recreate natural laws, including spatial environments in **Blender** and complex artificial life (ALife) engines that mirror ecosystem feedback loops.")

st.markdown("---")
# Quick Branch Return Navigation
if st.button("⬅️ Back to Computer Science Hub", use_container_width=True):
    st.switch_page("pages/3_💻_Computer_Science.py")
