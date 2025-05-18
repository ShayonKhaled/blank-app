import streamlit as st
from PIL import Image
import requests
import random

# App title
st.title("LLM-based Robot Control Interface")

# --- Live Camera Feed ---
st.subheader("Live Camera Feed")
image_url = "https://media.licdn.com/dms/image/v2/D4D22AQH8ndnQnKOmtQ/feedshare-shrink_800/feedshare-shrink_800/0/1697923969230?e=1750291200&v=beta&t=j6grdQiS47DmjT-hT398lHgKYhltJ5vz91Taqch402k"
image = Image.open(requests.get(image_url, stream=True).raw)
st.image(image, caption="Simulated camera stream with YOLOv8 overlay (for demonstration purposes only)", use_container_width=True)



# --- Command Input ---
st.subheader("Command Input")
user_command = st.text_input("Enter natural language command:")

# Simulated LLM Response
if user_command:
    responses = [
        "Moving toward the red object on the left.",
        "Object detected: bottle, 1.2 meters away.",
        "Executing pick-and-place sequence.",
        "Navigating to the drop-off zone."
    ]
    st.subheader("LLM Response")
    st.info(random.choice(responses))

# --- Robot Status ---
st.subheader("Robot Status")
col1, col2, col3 = st.columns(3)
col1.metric("Battery", "84%", "OK")
col2.metric("Mode", "Autonomous", "✅")
col3.metric("Status", "Navigating", "🚗")

# Footer
st.caption("Mockup UI created by team 25K02.")
