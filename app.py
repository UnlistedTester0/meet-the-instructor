import streamlit as st

# 1. REGISTER WORKING PAGES FROM THE UN-TRACKED FOLDER LOCATION
# Fixed the missing quote mark on the line below:
pages_matrix = [
    st.Page("src_pages/0_Main_Menu.py", title="Main Menu", icon="🚀", default=True),
    st.Page("src_pages/1_Get_To_know_Me.py", title="Get To Know Me", icon="ℹ️"),
    st.Page("src_pages/2_Exercise_Science.py", title="Exercise Science Study", icon="🏃‍♂️"),
    st.Page("src_pages/3_Computer_Science.py", title="Computer Science Hub", icon="💻"),
    st.Page("src_pages/3A_Hardware_Engineering.py", title="Hardware Engineering", icon="🔌"),
    st.Page("src_pages/3B_Software_Simulations.py", title="Software Simulations", icon="💾"),
    st.Page("src_pages/4_Rock_Climbing.py", title="Rock Climbing", icon="🧗"),
    st.Page("src_pages/5_Nutrition.py", title="Sports Nutrition", icon="🥗"),
    st.Page("src_pages/6_Learning_Plan.py", title="Weekly Learning Plan", icon="📋"),
]

# 2. RENDER THE SIDEBAR DIRECTORY CLEANLY
current_page = st.navigation(pages_matrix, position="sidebar")

# 3. EXECUTE THE APPMATRIX CONTROLLER RUNTIME
current_page.run()
