import streamlit as st
import streamlit.components.v1 as components

# Configure global window targets natively
st.set_page_config(page_title="STEM Main Menu", page_icon="🚀", layout="centered")

# --- PARENT NAVIGATION BANNER ---
# Placed right at the top of the screen to guide smartphone users instantly
st.info("ℹ️ **Mobile Users:** Tap the small **arrow icon ( << )** or two lines at the top-left corner of your screen to open the **Navigation Menu** and explore my background, climbing portfolio, and curriculum plan!")
st.markdown("---")

st.title("Welcome to the STEM Portal! 👋")
st.caption("🌌 YMCA After-School Enrichment App")

st.markdown("""
Thank you so much for taking the time to explore this space! I designed this interactive web app 
as a direct window into what I teach and what your children are exploring in our program. 

### 🪐 Full Interactive N-Body Gravity Simulator
Below is a simple interactive astrophysics laboratory.
* **Hypothesis: Can you send a planet into a stable orbit around the star? 
* **Tap/Click and hold** anywhere on the screen to anchor a point.
* **Drag your finger back** like a slingshot to build velocity.
* **Release** to launch a custom planet into the gravity matrix!
""")

# Original high-performance multi-body vector simulation loop
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
        
        // Massive central star coordinates
        const star = { x: canvas.width / 2, y: canvas.height / 2, mass: 1200, r: 22 };
        let planets = []; let touchStart = null; let currentTouch = null;

        function updatePhysics() {
            for (let i = planets.length - 1; i >= 0; i--) {
                let p = planets[i]; let dx = star.x - p.x; let dy = star.y - p.y;
                let distSq = dx * dx + dy * dy; let dist = Math.sqrt(distSq);
                if (dist < star.r + p.r) { planets.splice(i, 1); continue; }
                let force = star.mass / distSq; p.vx += (dx / dist) * force; p.vy += (dy / dist) * force;
                p.x += p.vx; p.y += p.vy;
                if (p.x < -100 || p.x > canvas.width + 100 || p.y < -100 || p.y > canvas.height + 100) { planets.splice(i, 1); }
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

# --- PRO TIP ELEMENT ---
# Positioned cleanly directly beneath the canvas viewframe boundary
st.warning("💡 **PRO TIP:** One of the best ways to learn in science is through failure and peer review!! If you can't get a planet into a stable orbit, refresh the page or even shoot multiple planets in one simulation and make some art!!!! Or you can ask someone else if they know how!")