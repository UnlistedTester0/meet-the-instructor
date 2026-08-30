import streamlit as st
import os

# 1. RADAR DETECTION LINK
# Automatically tracks whether your current folder is named 'modules', 'pages', or 'Pages'
folder = "modules" if os.path.exists("modules") else ("Pages" if os.path.exists("Pages") else "pages")

# Scans your folder and grabs the exact, real filenames on the server to prevent case-sensitive crashes
local_files = os.listdir(folder) if os.path.exists(folder) else []

def get_verified_path(prefix):
    """Finds the true filename matching our numeric file prefix layout."""
    for f in local_files:
        if f.startswith(prefix) and f.endswith(".py"):
            return f"{folder}/{f}"
    return None

# 2. CONSTRUCT VALID MATRIX MAP
pages_matrix = []

m0 = get_verified_path("0_")
m1 = get_verified_path("1_")
m2 = get_verified_path("2_")
m3 = get_verified_path("3_")
m3A = get_verified_path("3a_")
m3B = get_verified_path("3b_")
m4 = get_verified_path("4_")
m5 = get_verified_path("5_")
m6 = get_verified_path("6_")
m7 = get_verified_path("7_")
m8 = get_verified_path("8_")

# Safely register whatever file names are present in your online workspace
if m0: pages_matrix.append(st.Page(m0, title="Main Menu", icon="🚀", default=True))
if m1: pages_matrix.append(st.Page(m1, title="Get To Know Me", icon="ℹ️"))
if m2: pages_matrix.append(st.Page(m2, title="Exercise Science Study", icon="🏃‍♂️"))
if m3: pages_matrix.append(st.Page(m3, title="Computer Science Hub", icon="💻"))
if m3A: pages_matrix.append(st.Page(m3A, title="Hardware Engineering", icon="🔌"))
if m3B: pages_matrix.append(st.Page(m3B, title="Software Simulations", icon="💾"))
if m4: pages_matrix.append(st.Page(m4, title="Rock Climbing", icon="🧗"))
if m5: pages_matrix.append(st.Page(m5, title="Sports Nutrition", icon="🥗"))
if m6: pages_matrix.append(st.Page(m6, title="Weekly Learning Plan", icon="📋"))
if m7: pages_matrix.append(st.Page(m7, title="Adopt A Pixel", icon="🔭"))
if m8: pages_matrix.append(st.Page(m8, title="Philosophy & Stories", icon="🧠"))

# 3. POSITION SIDEBAR DIRECTORY
# Omitting app.py completely prevents the default ghost link from generating!
current_page = st.navigation(pages_matrix, position="sidebar")

# 4. RUN SYSTEM ENGINES
current_page.run()
