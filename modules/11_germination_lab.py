import streamlit as st

def run_page_11():
    st.title("🌱 Page 11: Interactive Seed Germination Lab")
    st.write("Click the buttons below to interact with the environment. Watch the canvas adapt in real-time!")

    # Initialize State Variables
    if "lab_seed_dropped" not in st.session_state:
        st.session_state.lab_seed_dropped = False
    if "lab_water_level" not in st.session_state:
        st.session_state.lab_water_level = 0
    if "lab_simulation_running" not in st.session_state:
        st.session_state.lab_simulation_running = False

    # Layout Columns - FIXED: Added required positional argument '2'
    col_controls, col_display = st.columns(2)

    with col_controls:
        st.subheader("🔬 Lab Controls")
        
        # Seed Control
        if st.button("🫳 Drop Seed into Soil", disabled=st.session_state.lab_seed_dropped):
            st.session_state.lab_seed_dropped = True
            st.rerun()

        # Water Control
        water_label = f"🫗 Pour Water ({st.session_state.lab_water_level}/3)"
        if st.button(water_label, disabled=not st.session_state.lab_seed_dropped or st.session_state.lab_water_level >= 3):
            st.session_state.lab_water_level += 1
            st.rerun()

        # Time Simulation Control
        sim_ready = st.session_state.lab_seed_dropped and st.session_state.lab_water_level >= 3
        if st.button("⏰ Start Day Cycle (Sun & Growth)", disabled=not sim_ready or st.session_state.lab_simulation_running):
            st.session_state.lab_simulation_running = True
            st.rerun()

        # Reset Environment
        if st.button("🔄 Reset Ecosystem"):
            st.session_state.lab_seed_dropped = False
            st.session_state.lab_water_level = 0
            st.session_state.lab_simulation_running = False
            st.rerun()

    with col_display:
        # Convert state variables to safe JS string flags
        seed_js = "true" if st.session_state.lab_seed_dropped else "false"
        run_sim_js = "true" if st.session_state.lab_simulation_running else "false"
        water_drops = st.session_state.lab_water_level

        # Embedded HTML5 Canvas Engine
        html_code = f"""
        <canvas id="labCanvas" width="500" height="350" style="border: 2px solid #333; border-radius: 8px; background: #e0f7fa;"></canvas>
        <script>
            const canvas = document.getElementById('labCanvas');
            const ctx = canvas.getContext('2d');

            // Lab Context Variables
            let seedDropped = {seed_js};
            let waterLevel = {water_drops};
            let runSimulation = {run_sim_js};

            // Animation Variables
            let timeStep = 0; 
            let stalkHeight = 0;
            let leafScale = 0;
            let flowerScale = 0;

            function draw() {{
                ctx.clearRect(0, 0, canvas.width, canvas.height);

                // 1. SKY COLORING (Transitions to dawn smoothly using native JS operations)
                let skyGradient = ctx.createLinearGradient(0, 0, 0, 250);
                if (runSimulation) {{
                    let progress = Math.min(timeStep / 150, 1);
                    let redVal = Math.floor(135 + (progress * 40));
                    let greenVal = Math.floor(206 - (progress * 50));
                    let bottomRed = Math.floor(255 - (progress * 20));
                    let bottomGreen = Math.floor(223 - (progress * 40));
                    
                    skyGradient.addColorStop(0, "rgb(" + redVal + ", " + greenVal + ", 250)");
                    skyGradient.addColorStop(1, "rgb(" + bottomRed + ", " + bottomGreen + ", 180)");
                }} else {{
                    skyGradient.addColorStop(0, '#87CEEB');
                    skyGradient.addColorStop(1, '#E0F6FF');
                }}
                ctx.fillStyle = skyGradient;
                ctx.fillRect(0, 0, canvas.width, 250);

                // 2. SUN MOVEMENT ENGINE (Explicit trajectory arc tracking)
                let sunX = 60;
                let sunY = 70;
                if (runSimulation) {{
                    sunX = 60 + (timeStep * 2.5);
                    sunY = 120 - 80 * Math.sin((timeStep / 150) * Math.PI);
                    if (sunX > canvas.width + 40) sunX = canvas.width + 40; 
                }}
                
                ctx.beginPath();
                ctx.arc(sunX, sunY, 30, 0, 2 * Math.PI);
                ctx.fillStyle = '#FFD700';
                ctx.shadowColor = '#FFA500';
                ctx.shadowBlur = 15;
                ctx.fill();
                ctx.shadowBlur = 0; 

                // 3. GROUND LAYERS
                ctx.fillStyle = '#8B5A2B';
                ctx.fillRect(0, 250, canvas.width, 100);
                ctx.fillStyle = '#6E4724';
                ctx.fillRect(0, 255, canvas.width, 5); 

                // 4. WATER INDICATOR OVERLAY
                if (waterLevel > 0) {{
                    ctx.fillStyle = "rgba(0, 191, 255, " + (waterLevel * 0.15) + ")";
                    ctx.fillRect(0, 250, canvas.width, 10);
                }}

                // 5. SEED RENDERING
                if (seedDropped && stalkHeight === 0) {{
                    ctx.beginPath();
                    ctx.ellipse(250, 265, 10, 6, Math.PI / 6, 0, 2 * Math.PI);
                    ctx.fillStyle = '#D2B48C';
                    ctx.fill();
                    ctx.lineWidth = 1.5;
                    ctx.strokeStyle = '#5C4033';
                    ctx.stroke();
                }}

                // 6. DYNAMIC PLANT GROWTH KERNEL
                if (runSimulation) {{
                    timeStep += 0.75;
                    if (timeStep > 40 && stalkHeight < 90) {{
                        stalkHeight += 0.6; 
                    }}
                    if (stalkHeight >= 50 && leafScale < 1) {{
                        leafScale += 0.02;
                    }}
                    if (stalkHeight >= 90 && flowerScale < 1) {{
                        flowerScale += 0.02;
                    }}
                }}

                // Draw Plant Structure
                if (stalkHeight > 0) {{
                    ctx.beginPath();
                    ctx.moveTo(250, 260);
                    ctx.quadraticCurveTo(245, 260 - stalkHeight/2, 250, 260 - stalkHeight);
                    ctx.lineWidth = 5;
                    ctx.strokeStyle = '#4CAF50';
                    ctx.lineCap = 'round';
                    ctx.stroke();

                    // Leaf Left
                    if (leafScale > 0) {{
                        ctx.save();
                        ctx.translate(248, 220);
                        ctx.scale(leafScale, leafScale);
                        ctx.beginPath();
                        ctx.ellipse(-10, -5, 12, 6, -Math.PI / 4, 0, 2 * Math.PI);
                        ctx.fillStyle = '#66BB6A';
                        ctx.fill();
                        ctx.restore();
                    }}

                    // Leaf Right
                    if (leafScale > 0) {{
                        ctx.save();
                        ctx.translate(252, 195);
                        ctx.scale(leafScale, leafScale);
                        ctx.beginPath();
                        ctx.ellipse(10, -5, 12, 6, Math.PI / 4, 0, 2 * Math.PI);
                        ctx.fillStyle = '#66BB6A';
                        ctx.fill();
                        ctx.restore();
                    }}

                    // Flower Head Growth - FIXED: Completed truncated JS code segment
                    if (flowerScale > 0) {{
                        let fY = 260 - stalkHeight;
                        ctx.save();
                        ctx.translate(250, fY);
                        ctx.scale(flowerScale, flowerScale);

                        ctx.fillStyle = '#FF69B4';
                        for (let i = 0; i < 6; i++) {{
                            ctx.beginPath();
                            ctx.arc(0, 0, 12, 0, 2 * Math.PI);
                            ctx.translate(0, -14);
                            ctx.fill();
                            ctx.translate(0, 14);
                            ctx.rotate(Math.PI / 3);
                        }}
                        
                        // Flower Center
                        ctx.beginPath();
                        ctx.arc(0, 0, 10, 0, 2 * Math.PI);
                        ctx.fillStyle = '#FFD700';
                        ctx.fill();
                        ctx.restore();
                    }}
                }}
                requestAnimationFrame(draw);
            }}
            draw();
        </script>
        """
        st.components.v1.html(html_code, height=360)

if __name__ == "__main__":
    run_page_11()
