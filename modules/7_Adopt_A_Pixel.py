import streamlit as st
import os

st.set_page_config(page_title="Adopt A Pixel", page_icon="🔭", layout="centered")

st.header("🔭 NASA 'Adopt a Pixel' Campaign")
st.subheader("Nancy Grace Roman Space Telescope Mission")

st.success("🚀 **Fresh Mission Update:** NASA's next-generation flagship observatory successfully blasted off into orbit on a SpaceX Falcon Heavy rocket! It is now traveling to its deep-space home roughly 1,000,000 miles behind Earth. The Nancy Grace Roman Space Telescope lifted off from NASA's Kennedy Space Center at 7:26 AM EDT (11:26 UTC) on August 30, 2026. The spacecraft cleanly left Earth orbit approximately 70 minutes post-launch, beginning its deep-space cruise toward the Sun-Earth L2 Lagrange point. For more details, visit NASA.")

st.markdown("""
### 🪐 Claim Your Piece of the Cosmos!
To celebrate this historic launch, NASA launched an official public outreach program. You and your children can **Adopt a Pixel** on one of the space telescope's very first astronomical survey images!

**How it works:**
1. Click the official NASA portal link below.
2. Enter your email address (NASA allows one unique pixel assignment per email address).
3. You will instantly be assigned a personal cosmic pixel number coordinate.
4. Download and print your official digital certificate to display on the fridge!
""")

with st.container(border=True):
    st.markdown("### 🔗 Official NASA Registration Portal")
    st.write("Click the button below to leave this local app and jump straight to NASA's secure government science portal:")
    
    # Large high-contrast link button targeting NASA's direct program URL
    st.link_button(
        "🌌 Register & Adopt Your Space Pixel Here", 
        "https://science.nasa.gov/mission/roman-space-telescope/adopt-a-pixel/",
        use_container_width=True
    )

st.markdown("---")
st.subheader("🔬 Telescope Classroom Core Facts")
st.write("""
*   **Massive Vision Grid:** The Roman Space Telescope features a massive camera array that captures a field of view **100 times larger** than the Hubble Space Telescope's infrared view in a single snapshot!
*   **Cosmic Detective:** Your child's pixel will be used to survey billions of distant stars and galaxies to study dark energy, hunt for wandering exoplanets, and map out the overarching structure of space-time.
""")

st.markdown("---")

# --- NEW VISUAL CERTIFICATE ZONE ---
# Positioned at the absolute bottom of the mission brief layout
cert_img_path = "pictures/nasa_certificate.jpg"  # Adjust extension to .png if necessary

with st.container(border=True):
    if os.path.exists(cert_img_path):
        st.image(cert_img_path, caption="📜 My Official NASA Nancy Grace Roman Space Telescope Adoption Certificate", width="stretch")
    else:
        st.info("📷 [Pictures Folder] nasa_certificate.jpg Visual Asset Placeholder")