import streamlit as st
import os

st.set_page_config(page_title="Rock Climbing", page_icon="🧗", layout="centered")

# TOP IMAGE ZONE
top_image_path = "Pictures/climbing_top.jpg"
if os.path.exists(top_image_path):
    st.image(top_image_path, width="stretch")

st.header("🧗 Climbing, Problem Solving & Training")

st.markdown("""
Rock climbing is more than just an athletic challenge—it is a physical puzzle. 
In the climbing world, we don't just say we 'climbed' a wall; we say we **solved a route**. 

To reach the top, a climber must use logic, spatial awareness, and planning to figure out 
where their center of gravity needs to shift before making a move. This exact process of breaking 
down a complex path into small, manageable steps is precisely how I teach kids to approach 
coding and hardware engineering!
""")

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

# BOTTOM IMAGE ZONE
bottom_image_path = "Pictures/summit_team.jpg"
if os.path.exists(bottom_image_path):
    st.image(bottom_image_path, width="stretch", caption="Reaching the top!")
