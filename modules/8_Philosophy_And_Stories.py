import streamlit as st

st.set_page_config(page_title="Philosophy & Stories", page_icon="🧠", layout="centered")

st.header("🧠 Philosophy & Cosmic Stories")
st.subheader("Exploring Big Questions Through Literature")

st.markdown("""
Welcome to the think-tank! This section is designed to introduce young minds to profound concepts 
about existence, logic, and reality by blending timeless storytelling with classic philosophical ideas.
""")

# --- SECTION 1: THE SOCRATIC SEEKER ---
with st.container(border=True):
    st.markdown("### 🏛️ The Socratic Seeker: Questions & Curiosity")
    st.write("""
    **The Big Idea:** Socrates taught us that true wisdom begins when we admit how much we do not know. 
    By asking 'Why?' and questioning everything—just like Plato recorded in his ancient dialogues—we learn 
    to think for ourselves instead of just following the crowd.
    """)
    st.info("""
    📖 **The Featherless Chicken Debacle:** We explore the famous clash between Plato and Diogenes! 
    When Plato proudly defined a human as a *'featherless biped'* (a two-legged creature with no feathers), 
    Diogenes plucked all the feathers off a chicken, brought it into the classroom, and shouted: 
    *'Behold, Plato's man!'* 
    
    This hilarious story teaches kids how definitions work, why logical details matter, and how peer 
    review helps us fix mistakes in science and programming!
    """)

# --- SECTION 2: EXISTENTIAL ADVENTURES ---
with st.container(border=True):
    st.markdown("### 🌌 Existential Adventures: Choice & Authenticity")
    st.write("""
    **The Big Idea:** Drawing inspiration from thinkers like Jean-Paul Sartre and Friedrich Nietzsche, 
    we explore what it means to live genuinely. We look at the beauty of taking responsibility for your 
    own actions, embracing choice, and learning how to stand strong when facing rejection or failure.
    """)
    st.caption("💡 **Core Lesson:** True strength isn't about being perfect; it's about defining who you are through the choices you make every single day.")

# --- SECTION 3: THE COSMIC PERSPECTIVE ---
with st.container(border=True):
    st.markdown("### 🪐 The Cosmic Perspective: Nature & Wonders")
    st.write("""
    **The Big Idea:** Merging the fluid, natural harmony of Alan Watts with the scientific awe of Carl Sagan, 
    we look at our connection to the universe. We teach kids that we aren't just separate observers dropped 
    into the world—we are a living, breathing part of a vast, interconnected cosmic tapestry.
    """)
    st.warning("✨ *'Somewhere, something incredible is waiting to be known.'* — Carl Sagan")
