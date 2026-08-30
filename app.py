import streamlit as st

# REGISTER YOUR CLEAN CHAPTERS FROM THE UN-TRACKED MODULES LOCATION
pages_matrix = [
    st.Page("modules/0_Main_Menu.py", title="Main Menu", icon="🚀", default=True),
    st.Page("modules/1_Get_To_know_Me.py", title="Get To Know Me", icon="ℹ️"),
    st.Page("modules/2_Exercise_Science.py", title="Exercise Science Study", icon="🏃‍♂️"),
    st.Page("modules/3_Computer_Science.py", title="Computer Science Hub", icon="💻"),
    st.Page("modules/3A_Hardware_Engineering.py", title="Hardware Engineering", icon="🔌"),
    st.Page("modules/3B_Software_Simulations.py", title="Software Simulations", icon="💾"),
    st.Page("modules/4_Rock_Climbing.py", title="Rock Climbing", icon="🧗"),
    st.Page("modules/5_Nutrition.py", title="Sports Nutrition", icon="🥗"),
    st.Page("modules/6_Learning_Plan.py", title="Weekly Learning Plan", icon="📋"),
]

# POSITION THE SIDEBAR MENUS NATIVELY
current_page = st.navigation(pages_matrix, position="sidebar")

# RUN THE APPMATRIX CONTROLLER ENGINE
current_page.run()
