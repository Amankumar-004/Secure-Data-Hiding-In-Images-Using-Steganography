import streamlit as st
import numpy as np
from PIL import Image
import io
import hashlib

# Helper Functions
def derive_key(password, length):
    """Derive a consistent key from password using SHA-256"""
    key = hashlib.sha256(password.encode()).digest()
    return bytes([key[i % len(key)] for i in range(length)])

def encrypt_image(image, msg, password):
    img = np.array(image.convert("RGB"))
    
    # Convert message to bytes
    msg_bytes = msg.encode('utf-8')
    key = derive_key(password, len(msg_bytes))
    encrypted_bytes = bytes([msg_bytes[i] ^ key[i] for i in range(len(msg_bytes))])
    
    # Store message length (4 bytes)
    msg_len = len(encrypted_bytes)
    length_bytes = msg_len.to_bytes(4, byteorder='big')
    
    # Check capacity
    total_bytes = 4 + msg_len
    if total_bytes > img.size:
        raise ValueError(f"Message too large for image. Max capacity: {img.size - 4} bytes")
    
    # Store data
    n, m, z = 0, 0, 0
    data = length_bytes + encrypted_bytes
    
    for byte in data:
        img[n, m, z] = byte
        z = (z + 1) % 3
        if z == 0:
            m = (m + 1) % img.shape[1]
            if m == 0:
                n = (n + 1) % img.shape[0]
    
    return Image.fromarray(img)

def decrypt_image(image, password):
    img = np.array(image.convert("RGB"))
    
    # Extract length
    n, m, z = 0, 0, 0
    length_bytes = []
    
    for _ in range(4):
        length_bytes.append(img[n, m, z])
        z = (z + 1) % 3
        if z == 0:
            m = (m + 1) % img.shape[1]
            if m == 0:
                n = (n + 1) % img.shape[0]
    
    msg_len = int.from_bytes(bytes(length_bytes), byteorder='big')
    
    # Validate message length
    max_capacity = img.shape[0] * img.shape[1] * 3 - 4
    if msg_len < 0 or msg_len > max_capacity:
        raise ValueError("Invalid message length. This might not be an encrypted image or it's corrupted.")
    
    # Extract encrypted message
    encrypted_bytes = []
    for _ in range(msg_len):
        encrypted_bytes.append(img[n, m, z])
        z = (z + 1) % 3
        if z == 0:
            m = (m + 1) % img.shape[1]
            if m == 0:
                n = (n + 1) % img.shape[0]
    
    # Decrypt with password-derived key
    key = derive_key(password, len(encrypted_bytes))
    decrypted_bytes = bytes([encrypted_bytes[i] ^ key[i] for i in range(len(encrypted_bytes))])
    
    # Try decoding with UTF-8, fallback to error message
    try:
        return decrypted_bytes.decode('utf-8')
    except UnicodeDecodeError:
        return "❌ Decryption failed! This usually means:\n" \
               "1. Wrong password was used\n" \
               "2. The image wasn't encrypted with this tool\n" \
               "3. The image is corrupted"

# Streamlit UI
st.set_page_config(page_title="Secure Image Steganography", layout="centered")
st.title("🔐 Secure Image Steganography")

option = st.radio("Choose an option", ["Encrypt", "Decrypt"], horizontal=True)

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if option == "Encrypt":
    message = st.text_area("Secret Message")
    password = st.text_input("Encryption Password", type="password")
    
    if st.button("Encrypt"):
        if not uploaded_file:
            st.warning("Please upload an image")
        elif not message:
            st.warning("Please enter a secret message")
        elif not password:
            st.warning("Please enter a password")
        else:
            try:
                img = Image.open(uploaded_file)
                result = encrypt_image(img, message, password)
                st.success("Message encrypted successfully!")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.image(result, caption="Encrypted Image", use_column_width=True)
                with col2:
                    st.image(uploaded_file, caption="Original Image", use_column_width=True)
                
                # Download
                img_bytes = io.BytesIO()
                result.save(img_bytes, format="PNG")
                st.download_button(
                    label="Download Encrypted Image",
                    data=img_bytes.getvalue(),
                    file_name="encrypted.png",
                    mime="image/png"
                )
            except ValueError as e:
                st.error(str(e))
            except Exception as e:
                st.error(f"Encryption failed: {str(e)}")

elif option == "Decrypt":
    password = st.text_input("Decryption Password", type="password")
    
    if st.button("Decrypt"):
        if not uploaded_file:
            st.warning("Please upload an image")
        elif not password:
            st.warning("Please enter the decryption password")
        else:
            try:
                img = Image.open(uploaded_file)
                decrypted_msg = decrypt_image(img, password)
                st.success("Decryption completed!")
                st.text_area("Result", decrypted_msg, height=200)
            except Exception as e:
                st.error(f"Decryption failed: {str(e)}")
