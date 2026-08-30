import streamlit as st

# 1. REGISTER YOUR CLEAN CHAPTERS FROM THE UN-TRACKED MODULES LOCATION
# Changing this directory path completely stops the automatic ghost link injection.
modules_matrix = [
    st.module("modules/0_Main_Menu.py", title="Main Menu", icon="🚀", default=True),
    st.module("modules/1_Get_To_know_Me.py", title="Get To Know Me", icon="ℹ️"),
    st.module("modules/2_Exercise_Science.py", title="Exercise Science Study", icon="🏃‍♂️"),
    st.module("modules/3_Computer_Science.py", title="Computer Science Hub", icon="💻"),
    st.module("modules/3A_Hardware_Engineering.py", title="Hardware Engineering", icon="🔌"),
    st.module("modules/3B_Software_Simulations.py", title="Software Simulations", icon="💾"),
    st.module("modules/4_Rock_Climbing.py", title="Rock Climbing", icon="🧗"),
    st.module("modules/5_Nutrition.py", title="Sports Nutrition", icon="🥗"),
    st.module("modules/6_Learning_Plan.py", title="Weekly Learning Plan", icon="📋"),
]

# 2. POSITION THE SIDEBAR MENUS NATIVELY
current_module = st.navigation(modules_matrix, position="sidebar")

# 3. RUN APPMATRIX CORE RUNTIME
current_module.run()
