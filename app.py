import streamlit as st
import cv2
import numpy as np

st.title('Real-Time Camera Feed with Streamlit')

# Initialize camera
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert BGR to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Overlay text
    cv2.putText(frame_rgb, 'Hello AR!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame
    st.image(frame_rgb, channels='RGB')

    if st.button('Stop'):
        break

cap.release()
