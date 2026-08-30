import streamlit as st

# 1. REGISTER THE MASTER ROUTING MATRIX
# Notice app.py itself is NOT in this list. It only acts as the router.
pages_matrix = [
    st.Page("pages/0_Main_Menu.py", title="Main Menu", icon="🚀", default=True),
    st.Page("pages/1_Get_To_Know_Me.py", title="Get To Know Me", icon="ℹ️"),
    st.Page("pages/2_Exercise_Science.py", title="Exercise Science Study", icon="🏃‍♂️"),
    st.Page("pages/3_Computer_Science.py", title="Computer Science Hub", icon="💻"),
    st.Page("pages/3A_Hardware_Engineering.py", title="Hardware Engineering", icon="🔌"),
    st.Page("pages/3B_Software_Simulations.py", title="Software Simulations", icon="💾"),
    st.Page("pages/4_Rock_Climbing.py", title="Rock Climbing", icon="🧗"),
    st.Page("pages/5_Nutrition.py", title="Sports Nutrition", icon="🥗"),
    st.Page("pages/6_Learning_Plan.py", title="Weekly Learning Plan", icon="📋"),
]

# 2. POPULATE THE NAVIGATION DIRECTORY IN THE SIDEBAR
current_page = st.navigation(pages_matrix, position="sidebar")

# 3. BOOT THE ACTIVE SCREEN NATIVELY
current_page.run()
