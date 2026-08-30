import streamlit as st

st.set_page_config(page_title="Learning Plan", page_icon="📋", layout="centered")

st.header("📋 Student Learning Plan")
st.subheader("YMCA After-School STEM Curriculum Calendar")

st.markdown("""
This calendar displays what concepts have been brought to the children's attention. 
Each module focuses on an interactive, hands-on activity designed to teach problem-solving and critical thinking.
""")

with st.expander("🌌 Week 1: Gravity Wells & Spacetime"):
    st.write("**Core Concept:** Learning how mass alters space to create orbits.")
    st.caption("🔬 Activity: Launching mobile-ready vector planet paths (See Main Menu).")

with st.expander("🪐 Week 2: Solar System Architecture (Coming Soon)"):
    st.write("**Core Concept:** Tracking circular distribution networks and rotational speeds.")
