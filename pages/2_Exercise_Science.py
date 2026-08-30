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

st.markdown("---")
st.subheader("📂 Explore My Specialties & Resources")

# ROW 1: Core Target Content Links
nav_row1_col1, nav_row1_col2 = st.columns(2)
with nav_row1_col1:
    if st.button("ℹ️ Get To Know Me Overview", use_container_width=True):
        st.switch_page("pages/1_Get_To_Know_Me.py")
with nav_row1_col2:
    if st.button("💻 Computer Science Skills", use_container_width=True):
        st.switch_page("pages/3_Computer_Science.py")

# ROW 2: Practical Application Focus Areas
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

# ROW 3: Return Destination Vector
PAGE_HOME_LOBBY = "pages/0_Main_Menu.py"

if st.button("⬅️ Back to Main Menu", use_container_width=True):
    st.switch_page(PAGE_HOME_LOBBY)