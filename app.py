import streamlit as st
import streamlit.components.v1 as components

# 1. REGISTER THE ROUTING MATRIX (Tell Streamlit all these sub-pages exist safely)
# This maps the clean, text-only python filenames you created earlier.
pages_matrix = [
    st.Page("app.py", title="Main Menu", icon="🚀"),
    st.Page("pages/1_Get_To_Know_Me.py", title="Get To Know Me", icon="ℹ️"),
    st.Page("pages/2_Exercise_Science.py", title="Exercise Science Study", icon="🏃‍♂️"),
    st.Page("pages/3_Computer_Science.py", title="Computer Science Hub", icon="💻"),
    st.Page("pages/3A_Hardware_Engineering.py", title="Hardware Engineering", icon="🔌"),
    st.Page("pages/3B_Software_Simulations.py", title="Software Simulations", icon="💾"),
    st.Page("pages/4_Rock_Climbing.py", title="Rock Climbing", icon="🧗"),
    st.Page("pages/5_Nutrition.py", title="Sports Nutrition", icon="🥗"),
    st.Page("pages/6_Learning_Plan.py", title="Weekly Learning Plan", icon="📋"),
]

# 2. INTRODUCE THE NAVIGATION CORE (Hide the default sidebar navigation map)
# This handles mobile optimization natively.
current_page = st.navigation(pages_matrix, position="hidden")

# 3. CONFIGURE GLOBAL WINDOW FRAME
st.set_page_config(page_title="STEM Main Menu", page_icon="🚀", layout="centered")

# --- MAIN PAGE GRAPHICS & MARKETING LOOP ---
st.title("Welcome to the STEM Portal! 👋")
st.caption("🌌 YMCA After-School Enrichment App")

st.markdown("""
Thank you so much for taking the time to explore this space! I designed this interactive web app 
as a direct window into what I teach and what your children are exploring in our program. 

### 🪐 Interactive Astro-Lab (Try It Out!)
Below is a live sample of one of my favorite subjects: **Astrophysics**. 
**Tap your phone screen**, pull back like a slingshot, and release to drop a miniature planet into orbit around the central star!
""")

# High-performance mobile touch-screen simulation engine string
simulation_js = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        body { margin: 0; padding: 0; background-color: #0b0f19; overflow: hidden; display: flex; justify-content: center; align-items: center; touch-action: none; }
        canvas { border: 2px solid #1e293b; border-radius: 12px; background: radial-gradient(circle at center, #0f172a 0%, #020617 100%); }
    </style>
</head>
<body>
    <canvas id="simCanvas"></canvas>
    <script>
        const canvas = document.getElementById('simCanvas'); const ctx = canvas.getContext('2d');
        const size = Math.min(window.innerWidth - 20, 450); canvas.width = size; canvas.height = size;
        const star = { x: canvas.width / 2, y: canvas.height / 2, mass: 800, r: 24 };
        let planets = []; let touchStart = null; let currentTouch = null;

        function updatePhysics() {
            for (let i = planets.length - 1; i >= 0; i--) {
                let p = planets[i]; let dx = star.x - p.x; let dy = star.y - p.y;
                let distSq = dx * dx + dy * dy; let dist = Math.sqrt(distSq);
                if (dist < star.r + p.r) { planets.splice(i, 1); continue; }
                let force = star.mass / distSq; p.vx += (dx / dist) * force; p.vy += (dy / dist) * force;
                p.x += p.vx; p.y += p.vy;
                if (p.x < -50 || p.x > canvas.width + 50 || p.y < -50 || p.y > canvas.height + 50) { planets.splice(i, 1); }
            }
        }
        function draw() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.beginPath(); ctx.arc(star.x, star.y, star.r, 0, Math.PI * 2); ctx.fillStyle = '#f59e0b'; ctx.fill();
            planets.forEach(p => { ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2); ctx.fillStyle = '#38bdf8'; ctx.fill(); });
            if (touchStart && currentTouch) {
                ctx.beginPath(); ctx.moveTo(touchStart.x, touchStart.y); ctx.lineTo(currentTouch.x, currentTouch.y);
                ctx.strokeStyle = '#ef4444'; ctx.lineWidth = 3; ctx.stroke();
            }
            updatePhysics(); requestAnimationFrame(draw);
        }
        canvas.addEventListener('pointerdown', (e) => {
            const rect = canvas.getBoundingClientRect();
            touchStart = { x: e.clientX - rect.left, y: e.clientY - rect.top }; currentTouch = { ...touchStart }; e.preventDefault();
        });
        canvas.addEventListener('pointermove', (e) => {
            if (!touchStart) return;
            const rect = canvas.getBoundingClientRect(); currentTouch = { x: e.clientX - rect.left, y: e.clientY - rect.top }; e.preventDefault();
        });
        canvas.addEventListener('pointerup', (e) => {
            if (!touchStart) return;
            planets.push({ x: touchStart.x, y: touchStart.y, vx: (touchStart.x - currentTouch.x) * 0.08, vy: (touchStart.y - currentTouch.y) * 0.08, r: 8 });
            touchStart = null; currentTouch = null; e.preventDefault();
        });
        draw();
    </script>
</body>
</html>
"""

components.html(simulation_js, height=470)

st.markdown("---")
st.subheader("📂 Explore the App Navigation")

# ROW 1: General Core Links
row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    if st.button("ℹ️ Get To Know Me", use_container_width=True):
        st.switch_page("pages/1_Get_To_Know_Me.py")
with row1_col2:
    if st.button("📋 Weekly Learning Plan", use_container_width=True):
        st.switch_page("pages/6_Learning_Plan.py")

# ROW 2: Academic Core Links
row2_col1, row2_col2 = st.columns(2)
with row2_col1:
    if st.button("🏃‍♂️ Exercise Science", use_container_width=True):
        st.switch_page("pages/2_Exercise_Science.py")
with row2_col2:
    if st.button("💻 Computer Science", use_container_width=True):
        st.switch_page("pages/3_Computer_Science.py")

# ROW 3: Specialization Links
row3_col1, row3_col2 = st.columns(2)
with row3_col1:
    if st.button("🧗 Rock Climbing", use_container_width=True):
        st.switch_page("pages/4_Rock_Climbing.py")
with row3_col2:
    if st.button("🥗 Sports Nutrition", use_container_width=True):
        st.switch_page("pages/5_Nutrition.py")

# 4. EXECUTE RUNTIME INJECTION COMMAND (Mandatory block for modern Streamlit compilation)
current_page.run()
