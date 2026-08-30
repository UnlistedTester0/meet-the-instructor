import streamlit as st

# 1. THE PRODUCTION MATRIX (Explicitly matching standard native rules)
pages_matrix = [
    st.Page("pages/0_main_menu.py", title="Main Menu", icon="🚀", default=True),
    st.Page("pages/1_get_to_know_me.py", title="Get To Know Me", icon="ℹ️"),
    st.Page("pages/2_exercise_science.py", title="Exercise Science Study", icon="🏃‍♂️"),
    st.Page("pages/3_computer_science.py", title="Computer Science Hub", icon="💻"),
    st.Page("pages/3a_hardware_engineering.py", title="Hardware Engineering", icon="🔌"),
    st.Page("pages/3b_software_simulations.py", title="Software Simulations", icon="💾"),
    st.Page("pages/4_rock_climbing.py", title="Rock Climbing", icon="🧗"),
    st.Page("pages/5_nutrition.py", title="Sports Nutrition", icon="🥗"),
    st.Page("pages/6_learning_plan.py", title="Weekly Learning Plan", icon="📋"),
]

# 2. POPULATE THE NAVIGATION DIRECTORY
current_page = st.navigation(pages_matrix, position="sidebar")

# 3. RUN RUNTIME ENGINE
current_page.run()
