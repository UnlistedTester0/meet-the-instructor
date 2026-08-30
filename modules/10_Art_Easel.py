import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Art Easel Lab", page_icon="🎨", layout="centered")

st.header("🖌️ The Interactive Art Easel")
st.subheader("Bob Ross Studio: Compact Workbench Layout")

st.markdown("""
Welcome to your side-by-side design workshop! Use the control dashboard on the left 
to instantly mix mediums, and sketch your concepts onto the canvas sheet.
""")

# High-performance scrollable side-by-side compact easel workshop system
easel_js = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        /* 📜 SCROLL INJECTION CHANNELS: Allows smooth vertical scrolling inside tight phone screens */
        html, body { 
            margin: 0; 
            padding: 5px; 
            background-color: #0b0f19; 
            font-family: sans-serif; 
            display: flex; 
            justify-content: center; 
            align-items: flex-start; 
            min-height: 100vh;
            overflow-y: auto !important; 
            -webkit-overflow-scrolling: touch;
        }
        
        /* Master Horizontal Grid Alignment Container Box */
        .workbench-layout { display: flex; flex-direction: row; gap: 15px; width: 100%; max-width: 650px; background: #0f172a; border: 2px solid #1e293b; border-radius: 12px; padding: 12px; box-sizing: border-box; }
        
        /* Left Column: Compact Adjustment Core */
        .control-tower { display: flex; flex-direction: column; width: 180px; flex-shrink: 0; }
        .control-group { background: #1e293b; border-radius: 8px; padding: 8px; margin-bottom: 8px; border: 1px solid #334155; }
        .group-title { font-size: 11px; font-weight: bold; color: #94a3b8; text-transform: uppercase; margin-bottom: 6px; letter-spacing: 0.5px; }
        
        /* Tool selection layouts */
        .tool-btn { width: 100%; background: #0f172a; border: 1px solid #475569; color: #94a3b8; padding: 6px; font-weight: bold; border-radius: 4px; cursor: pointer; font-size: 11px; margin-bottom: 4px; text-align: left; }
        .tool-btn.active { background: #3b82f6; color: white; border-color: #3b82f6; }
        
        /* Palette configuration */
        .palette-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; }
        .color-swatch { height: 26px; border-radius: 4px; border: 2px solid #0f172a; cursor: pointer; transition: transform 0.1s ease; }
        .color-swatch.active { border-color: #ffffff; transform: scale(1.05); }
        
        /* Slider sizing elements */
        .slider-row { display: flex; align-items: center; justify-content: space-between; color: #fff; font-size: 11px; font-weight: bold; }
        .brush-slider { width: 100%; cursor: pointer; margin-top: 4px; }
        
        /* Action buttons */
        .clear-btn { width: 100%; background: #ef4444; border: none; color: white; padding: 8px; font-weight: bold; border-radius: 6px; cursor: pointer; font-size: 12px; box-shadow: 0 3px 6px rgba(0,0,0,0.2); margin-top: 10px; }
        .clear-btn:active { background: #dc2626; }
        
        /* Right Column: Easel Visual Container Box */
        .easel-frame { background: #5c4033; border: 8px solid #3d2b1f; border-radius: 6px; padding: 10px; box-shadow: inset 0 0 15px rgba(0,0,0,0.6); display: flex; justify-content: center; align-items: center; flex-grow: 1; overflow: hidden; height: fit-content; }
        .canvas-container { position: relative; overflow: hidden; border: 3px solid #f8fafc; border-radius: 2px; }
        canvas { background-color: #ffffff; display: block; cursor: crosshair; }
        
        /* Page Rip Keyframe Trigger Classes */
        .rip-active { animation: ripSheet 0.4s ease-in forwards; }
        @keyframes ripSheet {
            0% { transform: translateY(0) rotate(0deg); opacity: 1; }
            100% { transform: translateY(350px) rotate(4deg); opacity: 0; }
        }

        /* Mobile Responsive Viewport Fallbacks */
        @media (max-width: 580px) {
            .workbench-layout { flex-direction: column; }
            .control-tower { width: 100%; }
            .palette-grid { grid-template-columns: repeat(6, 1fr); }
        }
    </style>
</head>
<body>

    <div class="workbench-layout">
        <!-- 🗼 LEFT COLUMN: CONTROL INTERFACE -->
        <div class="control-tower">
            <div class="control-group">
                <div class="group-title">🧰 Select Medium</div>
                <button class="tool-btn active" id="btn-paint" onclick="setTool('paint')">🎨 Paint Brush</button>
                <button class="tool-btn" id="btn-marker" onclick="setTool('marker')">🖊️ Chisel Marker</button>
                <button class="tool-btn" id="btn-spray" onclick="setTool('spray')">💨 Spray Paint</button>
            </div>
            
            <div class="control-group">
                <div class="group-title">🎨 Color Palette</div>
                <div class="palette-grid">
                    <div class="color-swatch active" style="background: #020617;" onclick="setColor('#020617', this)"></div>
                    <div class="color-swatch" style="background: #3b82f6;" onclick="setColor('#3b82f6', this)"></div>
                    <div class="color-swatch" style="background: #10b981;" onclick="setColor('#10b981', this)"></div>
                    <div class="color-swatch" style="background: #f59e0b;" onclick="setColor('#f59e0b', this)"></div>
                    <div class="color-swatch" style="background: #ef4444;" onclick="setColor('#ef4444', this)"></div>
                    <div class="color-swatch" style="background: #e2e8f0;" onclick="setColor('#e2e8f0', this)"></div>
                </div>
            </div>
            
            <div class="control-group">
                <div class="slider-row">
                    <span>Stroke Weight:</span>
                    <span id="sizeVal">10px</span>
                </div>
                <input type="range" id="brushSize" class="brush-slider" min="2" max="35" value="10" oninput="updateSize()">
            </div>
            
            <button class="clear-btn" onclick="triggerPageRip()">📄 New Sheet</button>
        </div>

        <!-- 🖼️ RIGHT COLUMN: IMAGE CANVAS SLATE -->
        <div class="easel-frame">
            <div class="canvas-container">
                <canvas id="paintCanvas"></canvas>
            </div>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('paintCanvas'); const ctx = canvas.getContext('2d');
        
        // Dynamically compute horizontal real-estate allocations
        const availableWidth = Math.min(window.innerWidth - 240, 400);
        const targetSize = availableWidth < 200 ? Math.min(window.innerWidth - 40, 320) : availableWidth;
        
        canvas.width = targetSize; canvas.height = targetSize * 0.8;
        
        let isPainting = false; let strokeColor = '#020617'; let strokeSize = 10; let brushType = 'paint';
        let lastPoint = null; let sprayInterval = null;

        clearCanvas();

        function draw(e) {
            if (!isPainting) return;
            const rect = canvas.getBoundingClientRect();
            const clientX = e.touches ? e.touches.clientX : e.clientX;
            const clientY = e.touches ? e.touches.clientY : e.clientY;
            const currentPoint = { x: clientX - rect.left, y: clientY - rect.top };
            
            if (brushType === 'spray') {
                lastPoint = currentPoint;
            } else {
                ctx.beginPath();
                if (lastPoint) ctx.moveTo(lastPoint.x, lastPoint.y);
                else ctx.moveTo(currentPoint.x, currentPoint.y);
                
                ctx.lineTo(currentPoint.x, currentPoint.y);
                ctx.strokeStyle = strokeColor; ctx.lineWidth = strokeSize;
                
                if (brushType === 'marker') { ctx.lineCap = 'square'; ctx.lineJoin = 'miter'; }
                else { ctx.lineCap = 'round'; ctx.lineJoin = 'round'; }
                
                ctx.stroke(); lastPoint = currentPoint;
            }
            e.preventDefault();
        }

        function generateSpray() {
            if (!isPainting || !lastPoint || brushType !== 'spray') return;
            const density = Math.min(strokeSize * 2, 50); ctx.fillStyle = strokeColor;
            for (let i = 0; i < density; i++) {
                const angle = Math.random() * Math.PI * 2; const radius = Math.random() * (strokeSize / 2);
                const x = lastPoint.x + Math.cos(angle) * radius; const y = lastPoint.y + Math.sin(angle) * radius;
                ctx.fillRect(x, y, 1.2, 1.2);
            }
        }

        function triggerPageRip() {
            if(canvas.classList.contains('rip-active')) return;
            canvas.classList.add('rip-active');
            setTimeout(() => {
                clearCanvas();
                canvas.classList.remove('rip-active');
            }, 400);
        }

        function setTool(tool) {
            brushType = tool;
            document.querySelectorAll('.tool-btn').forEach(b => b.classList.remove('active'));
            document.getElementById('btn-' + tool).classList.add('active');
            clearInterval(sprayInterval);
            if (tool === 'spray') sprayInterval = setInterval(generateSpray, 25);
        }

        function setColor(color, element) {
            strokeColor = color;
            document.querySelectorAll('.color-swatch').forEach(sw => sw.classList.remove('active'));
            element.classList.add('active');
        }

        function updateSize() { 
            strokeSize = document.getElementById('brushSize').value; 
            document.getElementById('sizeVal').innerText = strokeSize + 'px';
        }
        
        function clearCanvas() { ctx.fillStyle = '#ffffff'; ctx.fillRect(0, 0, canvas.width, canvas.height); ctx.beginPath(); }

        canvas.addEventListener('pointerdown', (e) => { 

            isPainting = true; 
            const rect = canvas.getBoundingClientRect();
            const clientX = e.touches ? e.touches.clientX : e.clientX;
            const clientY = e.touches ? e.touches.clientY : e.clientY;
            lastPoint = { x: clientX - rect.left, y: clientY - rect.top };
            if (brushType === 'spray') generateSpray(); else draw(e);
        });
        canvas.addEventListener('pointermove', draw);
        window.addEventListener('pointerup', () => { isPainting = false; lastPoint = null; });
    </script>
</body>
</html>
"""

components.html(easel_js, height=500)
