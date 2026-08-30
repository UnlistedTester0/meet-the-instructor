import streamlit as st

# 1. REGISTER THE MASTER ROUTING MATRIX WITH EXACT SERVER STRING PATHS
pages_matrix = [
    st.Page("pages/0_Main_Menu.py", title="Main Menu", icon="🚀", default=True),
    st.Page("pages/1_Get_To_know_Me.py", title="Get To Know Me", icon="ℹ️"),
    st.Page("pages/2_Exercise_Science.py", title="Exercise Science Study", icon="🏃‍♂️"),
    st.Page("pages/3_Computer_Science.py", title="Computer Science Hub", icon="💻"),
    st.Page("pages/3A_Hardware_Engineering.py", title="Hardware Engineering", icon="🔌"),
    st.Page("pages/3B_Software_Simulations.py", title="Software Simulations", icon="💾"),
    st.Page("pages/4_Rock_Climbing.py", title="Rock Climbing", icon="🧗"),
    st.Page("pages/5_Nutrition.py", title="Sports Nutrition", icon="🥗"),
    st.Page("pages/6_Learning_Plan.py", title="Weekly Learning Plan", icon="📋"),
]

# Populate the navigation sidebar menu cleanly
current_page = st.navigation(pages_matrix, position="sidebar")

# 2. INJECT CSS INJECTOR TO BLIND/HIDE THE BROKEN 'APP' SIDEBAR ELEMENT
# This targets the exact HTML sidebar text layout and sets it to display none.
st.markdown(
    """
    <style>
        [data-testid="stSidebarNav"] ul li:first-child {
            display: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Run the manager process
current_page.run()
