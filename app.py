import streamlit as st

# REGISTER THE MATRIX USING PLAIN TEXT STRINGS ONLY (Completely safe from emoji encoding bugs)
pages_matrix = [
    st.Page("modules/0_Main_Menu.py", title="Main Menu", default=True),
    st.Page("modules/1_Get_To_know_Me.py", title="Get To Know Me"),
    st.Page("modules/2_Exercise_Science.py", title="Exercise Science Study"),
    st.Page("modules/3_Computer_Science.py", title="Computer Science Hub"),
    st.Page("modules/3A_Hardware_Engineering.py", title="Hardware Engineering"),
    st.Page("modules/3B_Software_Simulations.py", title="Software Simulations"),
    st.Page("modules/4_Rock_Climbing.py", title="Rock Climbing"),
    st.Page("modules/5_Nutrition.py", title="Sports Nutrition"),
    st.Page("modules/6_Learning_Plan.py", title="Weekly Learning Plan"),
]

# Position the sidebar menu natively
current_page = st.navigation(pages_matrix, position="sidebar")

# Run the manager engine
current_page.run()
