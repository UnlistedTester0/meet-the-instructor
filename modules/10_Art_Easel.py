pythonimport streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Art Easel Lab", page_icon="🎨", layout="centered")
st.header("🖌️ The Interactive Art Easel")

easel_html = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        body { margin: 0; padding: 5px; background-color: #0b0f19; font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 90vh; overflow: hidden; touch-action: none; }
        .workbench-layout { display: flex; flex-direction: row; gap: 10px; width: 100%; background: #0f172a; border: 2px solid #1e293b; border-radius: 12px; padding: 10px; box-sizing: border-box; }
        .control-tower { display: flex; flex-direction: column; width: 110px; flex-shrink: 0; }
        .control-group { background: #1e293b; border-radius: 6px; padding: 6px; margin-bottom: 6px; }
        .tool-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2px; }
        .tool-btn { background: #0f172a; border: 1px solid #475569; color: #94a3b8; padding: 4px 1px; font-weight: bold; border-radius: 4px; cursor: pointer; font-size: 9px; text-align: center; }
        .tool-btn.active { background: #3b82f6; color: white; }
        .palette-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 4px; }
        .color-swatch { height: 22px; border-radius: 4px; cursor: pointer; border: 1px solid #0f172a; }
        .color-swatch.active { border-color: #fff; }
        .brush-slider { width: 100%; cursor: pointer; }
        .clear-btn { background: #ef4444; border: none; color: white; padding: 6px; font-weight: bold; border-radius: 4px; cursor: pointer; font-size: 11px; margin-top: 5px; }
        .easel-frame { background: #5c4033; border: 6px solid #3d2b1f; border-radius: 6px; padding: 8px; flex-grow: 1; display: flex; justify-content: center; }
        canvas { background: #ffffff; display: block; cursor: crosshair; border-radius: 2px; }
        .rip-active { animation: rip 0.4s ease-in forwards; }
        @keyframes rip { 100% { transform: translateY(350px) rotate(4deg); opacity: 0; } }
        @media (max-width: 450px) { .workbench-layout { flex-direction: column; } .control-tower { width: 100%; } .palette-grid { grid-template-columns: repeat(6, 1fr); } }
    </style>
</head>
<body>
    <div class="workbench-layout">
        <div class="control-tower">
            <div class="control-group"><div class="tool-grid"><button class="tool-btn active" id="btn-paint" onclick="setTool('paint')">🎨</button><button class="tool-btn" id="btn-marker" onclick="setTool('marker')">🖊️</button><button class="tool-btn" id="btn-spray" onclick="setTool('spray')">💨</button></div></div>
            <div class="control-group"><div class="palette-grid"><div class="color-swatch active" style="background:#020617" onclick="setColor('#020617',this)"></div><div class="color-swatch" style="background:#3b82f6" onclick="setColor('#3b82f6',this)"></div><div class="color-swatch" style="background:#10b981" onclick="setColor('#10b981',this)"></div><div class="color-swatch" style="background:#f59e0b" onclick="setColor('#f59e0b',this)"></div><div class="color-swatch" style="background:#ef4444" onclick="setColor('#ef4444',this)"></div><div class="color-swatch" style="background:#e2e8f0" onclick="setColor('#e2e8f0',this)"></div></div></div>
            <div class="control-group"><input type="range" id="brushSize" class="brush-slider" min="2" max="30" value="10" oninput="updateSize()"></div>
            <button class="clear-btn" onclick="triggerPageRip()">📄 Reset</button>
        </div>
        <div class="easel-frame"><canvas id="paintCanvas"></canvas></div>
    </div>
    <script>
        const canvas = document.getElementById('paintCanvas'); const ctx = canvas.getContext('2d');
        const target = Math.min(window.innerWidth - 160, 320); canvas.width = target < 150 ? window.innerWidth - 30 : target; canvas.height = canvas.width * 0.75;
        let isPainting = false; let strokeColor = '#020617'; let strokeSize = 10; let brushType = 'paint'; let lastPoint = null; let sprayInterval = null;
        clearCanvas();
        function getPos(e) { const r = canvas.getBoundingClientRect(); return { x: (e.clientX || e.touches[0].clientX) - r.left, y: (e.clientY || e.touches[0].clientY) - r.top }; }
        function draw(e) {
            if (!isPainting) return; const p = getPos(e);
            if (brushType === 'spray') { lastPoint = p; } else {
                ctx.beginPath(); ctx.moveTo(lastPoint.x, lastPoint.y); ctx.lineTo(p.x, p.y);
                ctx.strokeStyle = strokeColor; ctx.lineWidth = strokeSize; ctx.lineCap = brushType === 'marker' ? 'square' : 'round'; ctx.stroke(); lastPoint = p;
            }
            e.preventDefault();
        }
        function generateSpray() {
            if (!isPainting || !lastPoint || brushType !== 'spray') return; ctx.fillStyle = strokeColor;
            for (let i = 0; i < 30; i++) { const a = Math.random()*Math.PI*2; const r = Math.random()*(strokeSize/2); ctx.fillRect(lastPoint.x + Math.cos(a)*r, lastPoint.y + Math.sin(a)*r, 1.2, 1.2); }
        }
        function triggerPageRip() { if(canvas.classList.contains('rip-active')) return; canvas.classList.add('rip-active'); setTimeout(() => { clearCanvas(); canvas.classList.remove('rip-active'); }, 400); }
        function setTool(t) { brushType = t; document.querySelectorAll('.tool-btn').forEach(b => b.classList.remove('active')); document.getElementById('btn-'+t).classList.add('active'); clearInterval(sprayInterval); if (t === 'spray') sprayInterval = setInterval(generateSpray, 25); }
        function setColor(c, e) { strokeColor = c; document.querySelectorAll('.color-swatch').forEach(s => s.classList.remove('active')); e.classList.add('active'); }
        function updateSize() { strokeSize = document.getElementById('brushSize').value; }
        function clearCanvas() { ctx.fillStyle = '#ffffff'; ctx.fillRect(0, 0, canvas.width, canvas.height); ctx.lineJoin = 'round'; }
        canvas.addEventListener('pointerdown', (e) => { isPainting = true; lastPoint = getPos(e); if (brushType === 'spray') generateSpray(); else draw(e); });
        canvas.addEventListener('pointermove', draw); window.addEventListener('pointerup', () => { isPainting = false; lastPoint = null; });
    </script>
</body>
</html>
"""
components.html(easel_html, height=450)