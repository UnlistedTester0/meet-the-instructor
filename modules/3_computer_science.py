import streamlit as st

st.set_page_config(page_title="Computer Science", page_icon="💻", layout="centered")

st.header("💻 Computer Science & Engineering")
st.subheader("Languages, Hardware, & Custom Simulation Architecture")

st.markdown("""
My tech journey is rooted in deep curiosity, hands-on engineering, and understanding exactly what happens under the hood of a computer system. I split my focus between the physical silicon paths and the software algorithms that bring them to life.

Use the sidebar navigation drawer to explore the specific sub-branches:
* 🔌 **Hardware Engineering:** PCB design, circuit path mapping, and electronics assembly.
* 💾 **Software Simulations:** C++, Python, physics engines, and algorithmic modeling.
""")

st.markdown("---")
st.subheader("🔌 Interactive Hardware Lab: Breadboard Circuit Loops")
st.caption("Click different components below to see how physical electrical resistance alters voltage paths and dims the bulb!")

# INSERT THE HARDWARE SIMULATION ENGINE STRINGS HERE:
hardware_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; background-color: #0b0f19; font-family: sans-serif; color: #fff; overflow: hidden; }
        .hardware-canvas { border-radius: 8px; background: #020617; border: 1px dashed #334155; width: 100%; height: 200px; display: block; }
        .controls-row { display: flex; justify-content: space-around; margin-top: 12px; }
        .hw-btn { background: #1e293b; border: 1px solid #3b82f6; color: white; padding: 8px 16px; border-radius: 6px; cursor: pointer; font-weight: bold; }
    </style>
</head>
<body>
    <canvas id="hwCanvas" class="hardware-canvas"></canvas>
    <div class="controls-row">
        <button class="hw-btn" onclick="setResistor(0)">🔗 Wire Link (No Resistor)</button>
        <button class="hw-btn" onclick="setResistor(220)">📟 Add 220Ω Resistor</button>
        <button class="hw-btn" onclick="setResistor(1000)">📟 Add 1kΩ Resistor</button>
    </div>
    <script>
        const canvas = document.getElementById('hwCanvas'); const ctx = canvas.getContext('2d');
        let currentResistance = 0;
        function resizeCanvas() { canvas.width = canvas.parentElement.clientWidth; canvas.height = 180; drawCircuit(); }
        function setResistor(ohms) { currentResistance = ohms; drawCircuit(); }
        function drawCircuit() {
            ctx.clearRect(0, 0, canvas.width, canvas.height); const w = canvas.width; const h = canvas.height;
            let alpha = currentResistance === 0 ? 1.0 : (currentResistance === 220 ? 0.5 : 0.15);
            let glow = currentResistance === 0 ? '#f59e0b' : (currentResistance === 220 ? '#d97706' : '#b45309');
            ctx.fillStyle = '#ef4444'; ctx.fillRect(30, h/2 - 20, 30, 40); ctx.fillStyle = '#fff'; ctx.fillText('5V DC', 28, h/2 - 25);
            ctx.strokeStyle = '#64748b'; ctx.lineWidth = 4; ctx.beginPath(); ctx.moveTo(60, h/2); ctx.lineTo(120, h/2);
            ctx.moveTo(220, h/2); ctx.lineTo(w - 100, h/2); ctx.moveTo(w - 60, h/2); ctx.lineTo(w - 30, h/2); ctx.lineTo(w - 30, h - 20); ctx.lineTo(30, h - 20); ctx.lineTo(30, h/2 + 20); ctx.stroke();
            if (currentResistance === 0) { ctx.strokeStyle = '#10b981'; ctx.beginPath(); ctx.moveTo(120, h/2); ctx.lineTo(220, h/2); ctx.stroke(); ctx.fillStyle = '#10b981'; ctx.fillText('Copper Wire Link', 125, h/2 - 12); }
            else { ctx.strokeStyle = '#f59e0b'; ctx.beginPath(); ctx.moveTo(120, h/2); ctx.lineTo(135, h/2 - 15); ctx.lineTo(150, h/2 + 15); ctx.lineTo(165, h/2 - 15); ctx.lineTo(180, h/2 + 15); ctx.lineTo(195, h/2 - 15); ctx.lineTo(210, h/2 + 15); ctx.lineTo(220, h/2); ctx.stroke(); ctx.fillStyle = '#f59e0b'; ctx.fillText(currentResistance + ' \u03A9 Resistor', 130, h/2 - 22); }
            if(alpha > 0) { ctx.shadowBlur = 30 * alpha; ctx.shadowColor = '#f59e0b'; ctx.fillStyle = glow; ctx.beginPath(); ctx.arc(w - 80, h/2, 20, 0, Math.PI*2); ctx.fill(); ctx.shadowBlur = 0; }
            ctx.fillStyle = glow; ctx.beginPath(); ctx.arc(w - 80, h/2, 16, 0, Math.PI*2); ctx.fill(); ctx.fillStyle = '#475569'; ctx.fillRect(w - 85, h/2 + 15, 10, 10);
        }
        window.addEventListener('resize', resizeCanvas); setTimeout(resizeCanvas, 100);
    </script>
</body>
</html>
"""
import streamlit.components.v1 as components
components.html(hardware_html, height=260)