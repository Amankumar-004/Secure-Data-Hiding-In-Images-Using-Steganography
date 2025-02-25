import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

def select_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
    return file_path

def encrypt_image(image_path, msg, password):
    img = cv2.imread(image_path)
    if img is None:
        return "Error: Unable to load the image."

    msg_len = len(msg)
    length_bytes = msg_len.to_bytes(4, byteorder='big')  # Store length as 4 bytes

    d = {chr(i): i for i in range(256)}
    n, m, z = 0, 0, 0

    # Store message length in the first 4 pixels
    for byte in length_bytes:
        img[n, m, z] = byte
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    # Store the message
    for i in range(msg_len):
        img[n, m, z] = d[msg[i]]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    encrypted_image_path = os.path.join(os.path.dirname(image_path), "encryptedImage.png")
    cv2.imwrite(encrypted_image_path, img)
    return encrypted_image_path

def encrypt_button_clicked():
    image_path = select_image()
    if not image_path:
        return

    msg = encrypt_message_entry.get()
    password = encrypt_password_entry.get()

    if not msg or not password:
        messagebox.showerror("Error", "Please enter a message and password.")
        return

    encrypted_path = encrypt_image(image_path, msg, password)
    if "Error" in encrypted_path:
        messagebox.showerror("Error", encrypted_path)
        return

    messagebox.showinfo("Success", f"Image encrypted and saved as: {encrypted_path}")

    try:
        encrypted_image = Image.open(encrypted_path)
        new_window = tk.Toplevel(window)
        new_window.title("Encrypted Image")
        encrypted_image = ImageTk.PhotoImage(encrypted_image)
        image_label = tk.Label(new_window, image=encrypted_image)
        image_label.image = encrypted_image
        image_label.pack()
    except Exception as e:
        print(f"Error displaying image: {e}")

# GUI setup
window = tk.Tk()
window.title("Image Steganography - Encryption")

encrypt_frame = tk.LabelFrame(window, text="Encryption")
encrypt_frame.pack(pady=10)

encrypt_message_label = tk.Label(encrypt_frame, text="Message:")
encrypt_message_label.grid(row=0, column=0, padx=5, pady=5)
encrypt_message_entry = tk.Entry(encrypt_frame)
encrypt_message_entry.grid(row=0, column=1, padx=5, pady=5)

encrypt_password_label = tk.Label(encrypt_frame, text="Password:")
encrypt_password_label.grid(row=1, column=0, padx=5, pady=5)
encrypt_password_entry = tk.Entry(encrypt_frame, show="*")
encrypt_password_entry.grid(row=1, column=1, padx=5, pady=5)

encrypt_button = tk.Button(encrypt_frame, text="Encrypt", command=encrypt_button_clicked)
encrypt_button.grid(row=2, column=0, columnspan=2, pady=10)

window.mainloop()
