import streamlit as st
import os

# 1. DEFINE DETECTED TARGET DIRECTORY
folder = "src_pages" if os.path.exists("src_pages") else "pages"

# 2. RUN RADAR TO DETECT ACTUAL FILENAMES ON THE SERVER
local_files = os.listdir(folder) if os.path.exists(folder) else []

def find_file(prefix):
    """Finds the real filename matching our page order number prefix."""
    for f in local_files:
        if f.startswith(prefix) and f.endswith(".py"):
            return f"{folder}/{f}"
    return None

# 3. CONSTRUCT THE PAGES MATRIX DYNAMICALLY
# CRITICAL FIX: Removed st.Page("app.py") from this list to permanently stop the infinite recursion crash!
pages_matrix = []

# Map page slots safely by locating their ordering number prefix
p0 = find_file("0_")
p1 = find_file("1_")
p2 = find_file("2_")
p3 = find_file("3_")
p3A = find_file("3A_")
p3B = find_file("3B_")
p4 = find_file("4_")
p5 = find_file("5_")
p6 = find_file("6_")

# Safely append verified targets to the switchboard
if p0: pages_matrix.append(st.Page(p0, title="Main Menu Home", icon="🚀", default=True))
if p1: pages_matrix.append(st.Page(p1, title="Get To Know Me", icon="ℹ️"))
if p2: pages_matrix.append(st.Page(p2, title="Exercise Science Study", icon="🏃‍♂️"))
if p3: pages_matrix.append(st.Page(p3, title="Computer Science Hub", icon="💻"))
if p3A: pages_matrix.append(st.Page(p3A, title="Hardware Engineering", icon="🔌"))
if p3B: pages_matrix.append(st.Page(p3B, title="Software Simulations", icon="💾"))
if p4: pages_matrix.append(st.Page(p4, title="Rock Climbing", icon="🧗"))
if p5: pages_matrix.append(st.Page(p5, title="Sports Nutrition", icon="🥗"))
if p6: pages_matrix.append(st.Page(p6, title="Weekly Learning Plan", icon="📋"))

# 4. RENDER THE SIDEBAR DIRECTORY CLEANLY
current_page = st.navigation(pages_matrix, position="sidebar")

# 5. EXECUTE CURRENT CONTROLLER INSTANCE
current_page.run()
