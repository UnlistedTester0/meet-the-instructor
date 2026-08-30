import streamlit as st

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
