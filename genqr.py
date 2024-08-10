"""
A Streamlit app for generating colorful QR codes.

This script uses the Streamlit framework to create a web interface for 
generating QR codes with custom data, color, version, border, and resolution. 
The generated QR code is displayed as an image on the web page.

Imports:
    st (streamlit): The Streamlit library for creating web apps.
    genqr (function): A custom function from `qr.py` to generate QR codes.
    Image (PIL.Image): The Python Imaging Library (PIL) for handling images.

Functions:
    None
"""

import streamlit as st
from qr import genqr
from PIL import Image

st.title(':violet[Gen]:rainbow[QR] 🌚')

with st.form("custom-qr"):
    st.write("Generate Colourful QR Codes")
    data = st.text_input("Enter Some Data")
    color = st.color_picker("Choose Color", "#FF4B4B")
    version = st.slider("Choose QR Version", min_value=1, max_value=25, value=5)
    border = st.slider("Choose Border", min_value=0, max_value=5, value=3)
    size = st.slider("Choose Resolution", min_value=10, max_value=100, step=10, value=100)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        if not data:
            st.error("Please enter some data for the QR code.")
        else:
            qr = genqr(data, color, size, border, version)
            if "Something went wrong" in qr:
                st.error(qr)
            else:
                st.image(qr)
