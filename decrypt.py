import cv2
import hashlib
import numpy as np
import random

def generate_key(password):
    """Generate a hash-based key for random pixel selection."""
    return int(hashlib.sha256(password.encode()).hexdigest(), 16) % (10**8)

def retrieve_message(image, password):
    """Extract the hidden message from the image using password-based random selection."""
    
    # Generate the same random seed based on the password
    seed = generate_key(password)
    random.seed(seed)
    
    # Flatten the image into a 1D list of pixel values
    flat_img = image.flatten()
    
    # Generate random positions in the same order they were used for encryption
    total_pixels = len(flat_img)
    possible_bits = total_pixels // 3  # Maximum bits that can be stored
    indices = random.sample(range(total_pixels), possible_bits)
    
    # Extract binary data
    binary_data = ''.join(str(flat_img[i] & 1) for i in indices)
    
    # Find the end marker
    end_marker = '1111111111111110'
    end_position = binary_data.find(end_marker)
    
    if end_position != -1:
        binary_data = binary_data[:end_position]
    
    # Convert binary back to text
    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    extracted_text = "".join(chr(int(char, 2)) for char in chars)
    
    return extracted_text
