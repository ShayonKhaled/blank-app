import streamlit as st
from PIL import Image
import requests
import random

st.title("Robot Control Interface")

st.subheader("📹 Live Camera Feed")
image = Image.open(requests.get("https://picsum.photos/600/300", stream=True).raw)
st.image(image, caption="Simulated camera stream with YOLOv8 overlay", use_column_width=True)

st.subheader("💬 Command Input")
user_command = st.text_input("Enter natural language command:")

if user_command:
    responses = [
        "Moving toward the red object on the left.",
        "Object detected: bottle, 1.2 meters away.",
        "Executing pick-and-place sequence.",
        "Navigating to the drop-off zone."
    ]
    st.write("🧠 LLM Response:")
    st.info(random.choice(responses))

st.subheader("📡 Robot Status")
col1, col2, col3 = st.columns(3)
col1.metric("Battery", "84%", "⚡ OK")
col2.metric("Mode", "Autonomous", "✅")
col3.metric("Status", "Navigating", "🚗")

st.caption("Mockup UI created by team 25K02.")
