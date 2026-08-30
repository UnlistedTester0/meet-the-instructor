import streamlit as st

st.set_page_config(page_title="STEAM Portal", page_icon="🎨", layout="centered")

st.header("🎨 The STEAM Portal: Integrating Art")
st.subheader("Where Creative Design Meets Technical Engineering")

st.markdown("""
By shifting from STEM to **STEAM**, we introduce **Art & Design** into our technological playground. 
Behind every great video game engine, website, or piece of hardware is an artist who figured out 
how to make the technology beautiful, intuitive, and human.
""")

with st.container(border=True):
    st.markdown("### 🖥️ Graphic Design & Video Game Aesthetics")
    st.write("""
    Writing code handles the background math, but artists design the actual characters, worlds, and textures! 
    We teach kids how primitive geometric layouts are converted into beautiful 3D landscapes—including 
    modeling assets in software tools like **Blender** to give our digital worlds character and life.
    """)

with st.container(border=True):
    st.markdown("### 🪐 The Art of Science Visualization")
    st.write("""
    Complex physics formulas are just equations on paper until an artist translates them into high-fidelity visuals. 
    From drawing cosmic star formations to sketching out physical breadboard hardware wires, creative illustration 
    helps us communicate advanced engineering concepts clearly.
    """)

st.info("🎨 Use the sidebar navigation menu to jump into our live **Interactive Art Easel** to paint your own cosmic masterpiece!")
