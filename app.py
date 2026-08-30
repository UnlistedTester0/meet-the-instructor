import streamlit as st
import os

# Automatically detect whether your system uses 'pages' or 'Pages'
folder = "Pages" if os.path.exists("Pages") else "pages"

# 1. REGISTER THE ROUTING MATRIX WITH STREAMLIT
pages_matrix = [
    st.Page(f"{folder}/0_Main_Menu.py", title="Main Menu", icon="🚀"),
    st.Page(f"{folder}/1_Get_To_know_Me.py", title="Get To Know Me", icon="ℹ️"),
    st.Page(f"{folder}/2_Exercise_Science.py", title="Exercise Science Study", icon="🏃‍♂️"),
    st.Page(f"{folder}/3_Computer_Science.py", title="Computer Science Hub", icon="💻"),
    st.Page(f"{folder}/3A_Hardware_Engineering.py", title="Hardware Engineering", icon="🔌"),
    st.Page(f"{folder}/3B_Software_Simulations.py", title="Software Simulations", icon="💾"),
    st.Page(f"{folder}/4_Rock_Climbing.py", title="Rock Climbing", icon="🧗"),
    st.Page(f"{folder}/5_Nutrition.py", title="Sports Nutrition", icon="🥗"),
    st.Page(f"{folder}/6_Learning_Plan.py", title="Weekly Learning Plan", icon="📋"),
]

# 2. INTRODUCE THE NAVIGATION CORE (Hide the default sidebar navigation map)
current_page = st.navigation(pages_matrix, position="hidden")

# 3. RUN THE BOOT ROUTER (Launches your home lobby screen automatically)
current_page.run()
