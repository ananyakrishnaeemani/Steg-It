import cv2
import hashlib
import numpy as np
import random

def generate_key(password):
    """Generate a hash-based key for random pixel selection."""
    return int(hashlib.sha256(password.encode()).hexdigest(), 16) % (10**8)

def hide_message(image, message, password):
    """Embed a secret message in an image by modifying pixels at random positions."""

    # Generate a random seed from the password
    seed = generate_key(password)
    random.seed(seed)

    # Convert the message to binary
    binary_data = ''.join(format(ord(char), '08b') for char in message)
    binary_data += '1111111111111110'  # End marker

    # Get image properties
    height, width, _ = image.shape
    total_pixels = height * width * 3  # Each pixel has 3 color channels

    if len(binary_data) > total_pixels:
        raise ValueError("Message is too large to fit in the image.")

    # Generate random unique positions for embedding the binary data
    indices = list(range(total_pixels))
    random.shuffle(indices)
    indices = indices[:len(binary_data)]  # Select only required indices

    # Embed the message into the image
    img_copy = image.copy().flatten()  # Ensure mutable copy

    for i, bit in enumerate(binary_data):
        img_copy[indices[i]] = (img_copy[indices[i]] & 254) | int(bit)

    return img_copy.reshape(image.shape)
