import streamlit as st
from PIL import Image
import requests
import random

# App title
st.title("🤖 Robot Control Interface")

# --- Live Camera Feed ---
st.subheader("📷 Live Camera Feed")
image_url = "https://media.licdn.com/dms/image/D4D22AQGm5o4xjz0Jxw/feedshare-shrink_800/0/1689853678577?e=2147483647&v=beta&t=9Q1qkFqYwX7E0X2x9e0p7Rz2UeK3u5Fz1Z0Yb9h8ZcA"
image = Image.open(requests.get(image_url, stream=True).raw)
st.image(image, caption="Simulated camera stream with YOLOv8 overlay", use_container_width=True)

# --- Command Input ---
st.subheader("💬 Command Input")
user_command = st.text_input("Enter natural language command:")

# Simulated LLM Response
if user_command:
    responses = [
        "Moving toward the red object on the left.",
        "Object detected: bottle, 1.2 meters away.",
        "Executing pick-and-place sequence.",
        "Navigating to the drop-off zone."
    ]
    st.subheader("🧠 LLM Response")
    st.info(random.choice(responses))

# --- Robot Status ---
st.subheader("📡 Robot Status")
col1, col2, col3 = st.columns(3)
col1.metric("Battery", "84%", "⚡ OK")
col2.metric("Mode", "Autonomous", "✅")
col3.metric("Status", "Navigating", "🚗")

# Footer
st.caption("Mockup UI created by team 25K02.")
