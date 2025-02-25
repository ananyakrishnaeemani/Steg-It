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
        # Read uploaded image and convert it into OpenCV format
        uploaded_bytes = uploaded_image.read()
        image_array = np.frombuffer(uploaded_bytes, dtype=np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

        if image is None:
            st.error("Error loading the image. Please upload a valid image file.")
        else:
            # Hide message inside the image
            stego_image = hide_message(image, secret_text, security_key)

            # Save encoded image
            output_path = "encoded_image.png"
            cv2.imwrite(output_path, stego_image)

            st.image(stego_image, caption="Steganography Image (Looks Normal)", channels="BGR")
            st.download_button("Download Image", open(output_path, "rb").read(), "encoded_image.png", "image/png")

elif option == "Extract Message - (Decryption)":
    st.header("🔎 Retrieve Hidden Message from Image")

    encrypted_image = st.file_uploader("Upload an image with hidden text", type=["png", "jpg"])
    security_key = st.text_input("Enter the password", type="password")

    if encrypted_image and security_key:
        # Read uploaded image
        uploaded_bytes = encrypted_image.read()
        image_array = np.frombuffer(uploaded_bytes, dtype=np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

        if image is None:
            st.error("Error loading the image. Please upload a valid image file.")
        else:
            # Extract the hidden message
            extracted_text = retrieve_message(image, security_key)
            if extracted_text:
                st.success(f"Hidden Message: {extracted_text}")
            else:
                st.warning("No hidden message found or incorrect password.")
