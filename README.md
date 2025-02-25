# Image Steganography Tool 🔒

Welcome to the **Image Steganography Tool** repository! This tool allows you to hide secret messages inside images and retrieve them later using a password. It's a fun and secure way to share hidden information without anyone noticing.
https://encrypt-image-on-stego-it.streamlit.app/[https://encrypt-image-on-stego-it.streamlit.app/]

## Introduction

Steganography is the practice of concealing a message within another medium, such as an image, audio, or video file. This tool focuses on **image steganography**, where you can hide text messages inside an image file. The hidden message can only be retrieved using the correct password, ensuring security and privacy.


## Features

* **Encryption**: Hide a secret message inside an image using a password.
* **Decryption**: Retrieve the hidden message from the image using the correct password.
* **User-Friendly Interface**: Built with Streamlit for an intuitive and interactive experience.
* **Cross-Platform**: Works on any device with a web browser.


## How It Works

### Encryption Process
1. Upload an image (JPG or PNG).
2. Enter the secret message and a password.
3. The tool modifies the image's pixel values to embed the message in a random pattern based on the password.
4. Download the encoded image, which looks normal but contains the hidden message.

### Decryption Process
1. Upload the encoded image.
2. Enter the password used during encryption.
3. The tool extracts the hidden message by decoding the pixel values in the same random pattern.
