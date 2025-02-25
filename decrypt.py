import cv2
import tkinter as tk
from tkinter import filedialog, messagebox

def select_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
    return file_path

def decrypt_image(image_path, password):
    img = cv2.imread(image_path)
    if img is None:
        return "Error: Unable to load the image."

    c = {i: chr(i) for i in range(256)}
    message = ""
    n, m, z = 0, 0, 0

    # Read message length from the first 4 pixels
    length_bytes = bytearray()
    for _ in range(4):
        length_bytes.append(img[n, m, z])
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    message_length = int.from_bytes(length_bytes, byteorder='big')

    # Decrypt only the necessary pixels
    for i in range(message_length):
        message += c.get(img[n, m, z], '?') #replace any unknow character with "?"
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    return message

def decrypt_button_clicked():
    image_path = select_image()
    if not image_path:
        return

    password = decrypt_password_entry.get()

    if not password:
        messagebox.showerror("Error", "Please enter the password.")
        return

    decrypted_msg = decrypt_image(image_path, password)

    if "Error" in decrypted_msg:
        messagebox.showerror("Error", decrypted_msg)
        return

    decrypted_message_label.config(text=f"Decrypted Message: {decrypted_msg}")
    messagebox.showinfo("Success", f"Decrypted message: {decrypted_msg}")

# GUI for Decryption
window = tk.Tk()
window.title("Image Steganography - Decryption")

decrypt_frame = tk.LabelFrame(window, text="Decryption")
decrypt_frame.pack(pady=10)

decrypt_password_label = tk.Label(decrypt_frame, text="Password:")
decrypt_password_label.grid(row=0, column=0, padx=5, pady=5)
decrypt_password_entry = tk.Entry(decrypt_frame, show="*")
decrypt_password_entry.grid(row=0, column=1, padx=5, pady=5)

decrypt_button = tk.Button(decrypt_frame, text="Decrypt", command=decrypt_button_clicked)
decrypt_button.grid(row=1, column=0, columnspan=2, pady=10)

decrypted_message_label = tk.Label(decrypt_frame, text="Decrypted Message:")
decrypted_message_label.grid(row=2, column=0, columnspan=2, pady=5)

window.mainloop()
