import streamlit as st
import os

st.set_page_config(page_title="Rock Climbing", page_icon="🧗", layout="centered")

# --- 1. TOP IMAGE ZONE ---
top_image_path = "pictures/climbing_top.jpg"
if os.path.exists(top_image_path):
    st.image(top_image_path, width="stretch")
else:
    st.info("📷 [Pictures Folder] Top Climbing Visual Asset Placeholder")
# --------------------------

st.header("🧗 Climbing, Problem Solving & Training")

st.markdown("""
Rock climbing is more than just an athletic challenge—it is a physical puzzle. 
In the climbing world, we don't just say we 'climbed' a wall; we say we **solved a route**. 

To reach the top, a climber must use logic, spatial awareness, and planning to figure out 
where their center of gravity needs to shift before making a move. This exact process of breaking 
down a complex path into small, manageable steps is precisely how I teach kids to approach 
coding and hardware engineering!
""")

# Corrected biomechanics segment matching factual physical forces
with st.container(border=True):
    st.markdown("### 🧬 The Biomechanics of Climbing")
    st.write("""
    While a common misconception views rock climbing as a strict upper-body pulling sport, 
    true kinetic movement patterns prove otherwise. While the arms handle crucial vertical pulling adjustments, 
    climbing relies fundamentally on the **powerful upward pushing force of the legs**. 
    
    Leg-driven locomotion has carried humanity across the entire globe, and scaling a wall uses those same 
    primitive mechanisms. A **strong core** acts as the mandatory structural bridge—tightly synchronizing the 
    lower body's pushing drive with the upper body's stabilization loops to create a perfect harmony of pushing and pulling forces.
    """)

st.markdown("### 🏋️‍♂️ Supplemental Free-Weight Routine")
st.write("""
Because natural climbing movements are heavily integrated, standard conditioning can still leave isolated gaps. 
To preserve structural symmetry, safeguard joints, and ensure overall physical wellness, I substitute climbing 
with a structured free-weight routine focusing on antagonist muscle groups:
""")

# Clean column breakdown for the workout blueprint
col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):
        st.markdown("**💥 Core Pushing Movements**")
        st.write("""
        *   **Dumbbell Bench Press:** Targets chest and anterior deltoids.
        *   **Overhead Shoulder Press:** Strengthens vertical pushing stability.
        """)

with col2:
    with st.container(border=True):
        st.markdown("**🛡️ Structural Balance**")
        st.write("""
        *   **Tricep Dumbbell Extensions:** Counters heavy forearm/bicep pull strain.
        *   **Weighted Planks:** Reinforces straight-line power transfer.
        """)

st.markdown("---")

# --- 2. BOTTOM IMAGE ZONE ---
bottom_image_path = "pictures/summit_team.jpg"
if os.path.exists(bottom_image_path):
    st.image(bottom_image_path, width="stretch", caption="Reaching the top!")
else:
    st.info("📷 [Pictures Folder] Bottom Summit Visual Asset Placeholder")
# -----------------------------

st.markdown("---")
st.subheader("📂 Explore My Specialties & Resources")

# ROW 1: Academic Focus Areas
nav_row1_col1, nav_row1_col2 = st.columns(2)
with nav_row1_col1:
    if st.button("ℹ️ Get To Know Me Overview", use_container_width=True):
        st.switch_page("pages/1_Get_To_Know_Me.py")
with nav_row1_col2:
    if st.button("🏃‍♂️ Exercise Science Study", use_container_width=True):
        st.switch_page("pages/2️_Exercise_Science.py")

# ROW 2: Practical Application Focus Areas
nav_row2_col1, nav_row2_col2, nav_row2_col3 = st.columns(3)
with nav_row2_col1:
    if st.button("💻 Computer Science", use_container_width=True):
        st.switch_page("pages/3_Computer_Science.py")
with nav_row2_col2:
    if st.button("🥗 Sports Nutrition", use_container_width=True):
        st.switch_page("pages/5_Nutrition.py")
with nav_row2_col3:
    if st.button("📋 Learning Plan", use_container_width=True):
        st.switch_page("pages/6_Learning_Plan.py")

st.markdown("---")

# ROW 3: Return Destination Vector
if st.button("⬅️ Back to Main Menu", use_container_width=True):
    st.switch_page("app.py")
