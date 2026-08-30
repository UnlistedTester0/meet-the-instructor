import streamlit as st

st.set_page_config(page_title="Computer Science", page_icon="💻", layout="centered")

st.header("💻 Computer Science & Engineering")
st.subheader("Explore the Branches of Study")

st.markdown("""
My tech journey centers on understanding exactly what happens under the hood of a computer system. 
I split my focus between the physical silicon paths and the software algorithms that bring them to life.

Select a branch below to explore my projects, setups, and interactive tools:
""")

# Big Branch Selector Buttons
cs_col1, cs_col2 = st.columns(2)
with cs_col1:
    if st.button("🔌 Hardware & Engineering", use_container_width=True):
        st.switch_page("pages/3A_🔌_Hardware_Engineering.py")
with cs_col2:
    if st.button("💾 Software & Simulations", use_container_width=True):
        st.switch_page("pages/3B_💾_Software_Simulations.py")

st.markdown("---")
st.subheader("📂 Main App Navigation")

# Standardized Footer Rows
nav_row1_col1, nav_row1_col2 = st.columns(2)
with nav_row1_col1:
    if st.button("ℹ️ Get To Know Me Overview", use_container_width=True): st.switch_page("pages/1_Get_To_Know_Me.py")
with nav_row1_col2:
    if st.button("🏃‍♂️ Exercise Science Study", use_container_width=True): st.switch_page("pages/2_Exercise_Science.py")

nav_row2_col1, nav_row2_col2, nav_row2_col3 = st.columns(3)
with nav_row2_col1:
    if st.button("🧗 Rock Climbing", use_container_width=True): st.switch_page("pages/4_Rock_Climbing.py")
with nav_row2_col2:
    if st.button("🥗 Sports Nutrition", use_container_width=True): st.switch_page("pages/5_Nutrition.py")
with nav_row2_col3:
    if st.button("📋 Learning Plan", use_container_width=True): st.switch_page("pages/6_Learning_Plan.py")

st.markdown("---")
PAGE_HOME = "app.py"

# --- Your back button at the bottom stays the same ---
if st.button("⬅️ Back to Main Menu", use_container_width=True):
    st.switch_page(PAGE_HOME)