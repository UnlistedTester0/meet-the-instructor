import streamlit as st

st.set_page_config(page_title="Hardware Engineering", page_icon="🔌", layout="centered")

st.header("🔌 Hardware Engineering & Electronics")
st.subheader("Silicon, Breadboards, & Custom Circuit Design")

st.markdown("""
Code needs a physical highway to travel on. I love teaching how electricity is routed through circuits 
to process binary computational logic.
""")

with st.container(border=True):
    st.markdown("#### ⚡ PCB Layout & Custom Circuitry")
    st.write("I utilize industry-standard software tools like **KiCad** to map logic paths, test electrical integrity, and lay out prototype printed circuit boards from scratch.")

with st.container(border=True):
    st.markdown("#### 💾 Physical Breadboard Computing")
    st.write("I construct complex digital hardware blocks manually on breadboards—following low-level computing architectures like logic gates (74LS series) and microcontrollers (Arduino/C++) to understand components at an atomic level.")

st.markdown("---")
# Quick Branch Return Navigation
if st.button("⬅️ Back to Computer Science Hub", use_container_width=True):
    st.switch_page("src_pages/3_💻_Computer_Science.py")
