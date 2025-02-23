import streamlit as st
import cv2
import numpy as np
from encrypt import hide_message
from decrypt import retrieve_message

st.title("🔒 Image Steganography Tool")

# Sidebar Menu
option = st.sidebar.selectbox("Choose an option:", ["Embed Message - (Encryption)", "Extract Message - (Decryption)"])

if option == "Embed Message - (Encryption)":
    st.header("🖼️ Hide a Secret Message in an Image")
    
    uploaded_image = st.file_uploader("Upload an image file", type=["jpg", "png"])
    secret_text = st.text_area("Enter the message to hide")
    security_key = st.text_input("Enter a password", type="password")

    if uploaded_image and secret_text and security_key:
        # Read the uploaded file and convert it into an OpenCV image format
        image_bytes = np.frombuffer(uploaded_image.read(), dtype=np.uint8)
        image = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)

        # Hide message inside the image
        stego_image = hide_message(image, secret_text, security_key)
        cv2.imwrite("encoded_image.png", stego_image)
        
        st.image(stego_image, caption="Steganography Image (Looks Normal)", channels="BGR")
        st.download_button("Download Image", open("encoded_image.png", "rb").read(), "encoded_image.png", "image/png")

elif option == "Extract Message - (Decryption)":
    st.header("🔎 Retrieve Hidden Message from Image")
    
    encrypted_image = st.file_uploader("Upload an image with hidden text", type=["png", "jpg"])
    security_key = st.text_input("Enter the password", type="password")

    if encrypted_image and security_key:
        # Read the uploaded file
        image_bytes = np.frombuffer(encrypted_image.read(), dtype=np.uint8)
        image = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)

        # Extract the hidden message
        extracted_text = retrieve_message(image, security_key)
        st.success(f"Hidden Message: {extracted_text}")
