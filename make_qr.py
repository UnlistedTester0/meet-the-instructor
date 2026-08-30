import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

# 1. GENERATE A STABLE LEVEL-H HIGH-ERROR-CORRECTION CORE MATRIX
qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # 🛑 Grants 30% center block protection
    box_size=15,
    border=4,
)

# Replace with your actual live Streamlit Community Cloud web address link!
qr.add_data("https://streamlit.app")
qr.make(fit=True)

# Create a clean monochrome image base
qr_img = qr.make_image(fill_color="#020617", back_color="#ffffff").convert("RGBA")

# 2. DESIGN THE COMPACT CENTER BANNER TEXT CAP
draw = ImageDraw.Draw(qr_img)
w, h = qr_img.size

# Establish a solid white protective rectangle card in the exact center
banner_w, banner_h = 280, 80
x1, y1 = (w - banner_w) // 2, (h - banner_h) // 2
x2, y2 = x1 + banner_w, y1 + banner_h

# Draw the background border badge over the center pixels
draw.rectangle([x1, y1, x2, y2], fill="#ffffff", outline="#3b82f6", width=4)

# Write the text lines cleanly inside the badge window
# (Note: Using default layout font, you can substitute a true .ttf file path if preferred)
try:
    font = ImageFont.truetype("arial.ttf", 14)
except IOError:
    font = ImageFont.load_default()

# Overlay your custom text loops cleanly
draw.text((w//2, h//2 - 18), "I'm Matthew 👋", fill="#020617", font=font, anchor="mm")
draw.text((w//2, h//2 + 10), "Scan to learn about our class!", fill="#3b82f6", font=font, anchor="mm")

# 3. SAVE FRESH PRODUCTION ASSET DIRECTLY
os.makedirs("qr_code", exist_ok=True)
qr_img.save("qr_code/matthew_class_qr.png")
print("🚀 Customized text-integrated QR Code generated inside qr_code/ folder successfully!")
