import streamlit as st

# DEFINE STANDARDIZED NAVIGATION TARGETS
PAGE_HOME = "app.py"
PAGE_BIO = "pages/1_Get_To_Know_Me.py"
PAGE_EXERCISE = "pages/2_Exercise_Science.py"
PAGE_CS_HUB = "pages/3_Computer_Science.py"
PAGE_CLIMBING = "pages/4_Rock_Climbing.py"
PAGE_CURRICULUM = "pages/6_Learning_Plan.py"

st.set_page_config(page_title="Sports Nutrition", page_icon="🥗", layout="centered")

st.header("🥗 Nutrition as Fuel & Recovery")

st.markdown("""
Just like building a high-end desktop computer requires a high-efficiency power supply, a body 
handling complex mental puzzles and heavy physical movement requires clean nutritional fueling. 

Whether recovering from a climbing session or keeping high focus during a long study loop, 
understanding food macros keeps our system running optimally.
""")

with st.container(border=True):
    st.markdown("#### ⚡ Carbohydrates: The Main Power Grid")
    st.write("Carbs are the body's preferred primary energy source, critical for both muscle bursts and high-level brain glucose optimization during logic exercises.")

with st.container(border=True):
    st.markdown("#### 🛠️ Proteins: The Structural Maintenance Team")
    st.write("Essential for cell blueprint rebuilding and muscular tissue recovery after strenuous climbing or weight training sessions.")

with st.container(border=True):
    st.markdown("#### 🔋 Healthy Fats: Long-Term System Stability")
    st.write("Crucial for cellular membrane protection, joint lubrication, and maintaining steady hormone regulation over long hours.")

st.info("💡 **Fun Lesson Link:** I love showing the kids that nutrients are exactly like input variables in a software loop—what you put into the system directly dictates the performance output!")

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
    if st.button("📋 Learning Plan", use_container_width=True):
        st.switch_page(PAGE_CURRICULUM)

st.markdown("---")
if st.button("⬅️ Back to Main Menu", use_container_width=True):
    st.switch_page(PAGE_HOME)
