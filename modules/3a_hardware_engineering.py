import streamlit as st
import os

st.set_page_config(page_title="Hardware Engineering", page_icon="🔌", layout="centered")

st.header("🔌 Hardware Engineering & Electronics")
st.subheader("Silicon, Breadboards, & Custom Circuit Design")

st.markdown("""
Code needs a physical highway to travel on. I love teaching how electricity is routed through circuits 
to process binary computational logic.
""")

# --- SECTION 1: PCB DESIGN & KICAD FOOTPRINT ---
with st.container(border=True):
    st.markdown("#### ⚡ PCB Layout & Custom Circuitry")
    st.write("""
    I utilize industry-standard software tools like **KiCad** to map logic paths, test electrical integrity, 
    and lay out prototype printed circuit boards from scratch. This includes working with high-density, 
    advanced computing geometries like multi-layered surface mount footprints.
    """)
    
    # KiCad Footprint Visual Asset
    pcb_img = "Pictures/DDR5Footprint.png"
    if os.path.exists(pcb_img):
        st.image(pcb_img, caption="🎛️ Custom DDR5 Component Footprint inside KiCad Mapping Matrix", width="stretch")
    else:
        st.info("📷 [Pictures Folder] DDR5 Footprint Asset Placeholder")

# --- SECTION 2: PHYSICAL BREADBOARD ARCHITECTURE ---
with st.container(border=True):
    st.markdown("#### 💾 Physical Breadboard Computing")
    st.write("""
    I construct complex digital hardware blocks manually on breadboards—following low-level computing 
    architectures like logic gates (74LS series) and microcontrollers (Arduino/C++) to understand 
    components at an atomic level. 
    
    Building an 8-bit computer system requires mapping distinct logical sub-modules: tracking the master 
    clock timing channels, stabilizing the Memory Address Register (MAR), wiring the 16-byte random access memory cells, 
    and establishing clean data entry bus lines.
    """)

# --- SECTION 3: VERTICAL IMAGE STACK (Updated Orientation) ---
# Separating into individual vertical content cards gives each layout full wide visibility
with st.container(border=True):
    schematic_img = "Pictures/schematic_drawing.jpg"
    if os.path.exists(schematic_img):
        st.image(schematic_img, caption="📝 Logic Blueprints: Clock, MAR, 16-Byte Memory & Bus Links", width="stretch")
    else:
        st.info("📷 [Pictures Folder] Paper Schematics Asset Placeholder")

with st.container(border=True):
    power_img = "Pictures/breadboard_power.jpg"
    if os.path.exists(power_img):
        st.image(power_img, caption="⚡ Operational Phase: Integrated Sub-Modules Connected to Power", width="stretch")
    else:
        st.info("📷 [Pictures Folder] Physical Power Board Asset Placeholder")
