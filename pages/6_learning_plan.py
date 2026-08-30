import streamlit as st

# 1. DEFINE STANDARDIZED NAVIGATION TARGETS
PAGE_HOME = "app.py"
PAGE_BIO = "pages/1_Get_To_Know_Me.py"
PAGE_EXERCISE = "pages/2_Exercise_Science.py"
PAGE_CS_HUB = "pages/3_Computer_Science.py"
PAGE_CLIMBING = "pages/4_Rock_Climbing.py"
PAGE_NUTRITION = "pages/5_Nutrition.py"

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

st.markdown("---")
st.subheader("📂 Explore My Specialties & Resources")

# ROW 1: Academic Focus Areas
nav_row1_col1, nav_row1_col2 = st.columns(2)
with nav_row1_col1:
    if st.button("ℹ️ Get To Know Me Overview", use_container_width=True):
        st.switch_page(PAGE_BIO)
with nav_row1_col2:
    if st.button("🏃‍♂️ Exercise Science Study", use_container_width=True):
        st.switch_page(PAGE_EXERCISE)

# ROW 2: Practical Application Focus Areas
nav_row2_col1, nav_row2_col2, nav_row2_col3 = st.columns(3)
with nav_row2_col1:
    if st.button("💻 Computer Science", use_container_width=True):
        st.switch_page(PAGE_CS_HUB)
with nav_row2_col2:
    if st.button("🧗 Rock Climbing", use_container_width=True):
        st.switch_page(PAGE_CLIMBING)
with nav_row2_col3:
    if st.button("🥗 Sports Nutrition", use_container_width=True):
        st.switch_page(PAGE_NUTRITION)

st.markdown("---")

# ROW 3: Return Destination Vector
if st.button("⬅️ Back to Main Menu", use_container_width=True):
    st.switch_page(PAGE_HOME)
