import streamlit as st

st.set_page_config(page_title="Software Simulations", page_icon="💾", layout="centered")

st.header("💾 Software Engineering & Simulations")
st.subheader("Custom Code Engines & Physical Systems modeling")

st.markdown("""
Writing code isn't just about outputting data—it's about building virtual worlds. I create standalone engines 
and math environments to study complex physical interactions.
""")

with st.container(border=True):
    st.markdown("#### ⚙️ Low-Level Programming Languages")
    st.write("I develop cross-platform systems and custom logic matrices utilizing highly efficient development languages like **Python and C++**.")

with st.container(border=True):
    st.markdown("#### 🧬 Custom Physics & ALife Systems")
    st.write("I design algorithms that recreate natural laws, including spatial environments in Blender...")

st.markdown("---")
st.subheader("💾 Interactive Software Lab: Code Modification")
st.caption("Change the numerical variable inside the logic script below to dim or brighten the microcontroller's onboard LED indicator output!")

# INSERT THE SOFTWARE SUB-SIMULATION CODES HERE:
software_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; background-color: #0b0f19; font-family: sans-serif; color: #fff; overflow: hidden; }
        .code-editor { background: #020617; border: 1px solid #334155; font-family: monospace; border-radius: 8px; padding: 12px; color: #38bdf8; font-size: 14px; line-height: 1.5; }
        .code-input-line { color: #f59e0b; display: inline-flex; align-items: center; background: #1e293b; padding: 2px 6px; border-radius: 4px; border: 1px solid #475569; }
        .code-field { background: transparent; border: none; color: #ef4444; font-family: monospace; font-size: 14px; width: 50px; text-align: center; font-weight: bold; }
        .bulb-display { width: 100%; height: 110px; display: flex; justify-content: center; align-items: center; margin-top: 12px; border-radius: 8px; background: #020617; border: 1px solid #1e293b; }
        .bulb-svg { width: 70px; height: 70px; transition: filter 0.1s ease; }
    </style>
</head>
<body>
    <div class="code-editor">
        <span style="color:#64748b;">// Microcontroller Logic Pipeline Setup</span><br>
        <span style="color:#f43f5e;">import</span> machine<br>
        led = machine.PWM(machine.Pin(<span style="color:#ae81ff;">2</span>))<br><br>
        <span style="color:#64748b;">// Alter duty cycle variable limits (Value input range: 0 to 255)</span><br>
        led.brightness = <div class="code-input-line"><input type="number" id="brightnessInput" class="code-field" value="255" min="0" max="255" oninput="updateSoftwareBulb()"></div>
    </div>
    <div class="bulb-display">
        <svg id="swBulb" class="bulb-svg" viewBox="0 0 24 24" fill="none" xmlns="http://w3.org">
            <path d="M12 2C8.14 2 5 5.14 5 9C5 11.38 6.19 13.47 8 14.74V17C8 17.55 8.45 18 9 18H15C15.55 18 16 17.55 16 17V14.74C17.81 13.47 19 11.38 19 9C19 5.14 15.86 2 12 2Z" fill="#334155"/>
            <path d="M9 21C9 21.55 9.45 22 10 22H14C14.55 22 15 21.55 15 21V20H9V21Z" fill="#475569"/>
        </svg>
    </div>
    <script>
        function updateSoftwareBulb() {
            let val = parseInt(document.getElementById('brightnessInput').value);
            if(isNaN(val) || val < 0) val = 0; if(val > 255) val = 255;
            const bulb = document.getElementById('swBulb'); const factor = val / 255;
            if(val === 0) { bulb.style.filter = 'none'; bulb.querySelector('path').setAttribute('fill', '#334155'); }
            else { bulb.style.filter = `drop-shadow(0px 0px ${20 * factor}px rgba(245, 158, 11, ${factor}))`; bulb.querySelector('path').setAttribute('fill', `rgba(245, 158, 11, ${0.3 + (0.7 * factor)})`); }
        }
        setTimeout(updateSoftwareBulb, 100);
    </script>
</body>
</html>
"""
import streamlit.components.v1 as components
components.html(software_html, height=310)