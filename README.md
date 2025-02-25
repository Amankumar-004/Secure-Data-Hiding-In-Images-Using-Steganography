# 🖼️🔒 Image Steganography using Python

Image steganography is the technique of hiding a secret message within an image in such a way that the original image remains unaltered to the human eye.

## 🔍 Overview

This project provides a Python-based steganography tool that allows users to securely embed text messages within image files. The tool uses separate encryption (`encrypt.py`) and decryption (`decrypt.py`) programs. The encryption program hides the message, producing an encrypted image. The decryption program retrieves the hidden message. This solution ensures confidential communication via image-based steganography.

## 🚀 Features

-   **Secure Embedding:** Securely embed text messages within image files.
-   **Encryption:** Encrypt and hide messages.
-   **Output Image:** Generate encrypted images (e.g., `encryptedImage.png`).
-   **Decryption Program:** Retrieve and display hidden messages.
-   **Confidential Communication:** Ensure message confidentiality.
-   **Message Length Handling:** Encrypt and decrypt messages by storing and reading the message length within the image.
-   **User-Friendly GUI:** Simple graphical interface to encrypt and decrypt images.

## Requirements

This project requires the following Python libraries:

-   **OpenCV (opencv-python):** Used for image processing, specifically reading and writing image data.
-   **Tkinter (built-in):** Used for creating the graphical user interface (GUI).
-   **PIL (Pillow):** Used for image display in the GUI.
-   **NumPy:** Used for numerical operations, specifically for byte array conversions.


## Installation

1.  **Install Python:** Ensure you have Python 3.x installed on your system. You can download it from the official Python website (python.org).

2.  **Install OpenCV, Pillow, and NumPy:** Open a terminal or command prompt and run the following command to install the necessary packages using pip:

    ```bash
    pip install opencv-python pillow numpy
    ```

## Usage

1.  **Encryption:**
    -   Run the `encrypt.py` script.
    -   Select an image file using the file dialog.
    -   Enter the message you want to hide.
    -   Enter a password (note: this password is only used for GUI validation and does not actually encrypt the data).
    -   The encrypted image will be saved as `encryptedImage.png` in the same directory as the original image.

2.  **Decryption:**
    -   Run the `decrypt.py` script.
    -   Select the encrypted image file using the file dialog.
    -   Enter the password (note: this password is only used for GUI validation and does not actually decrypt the data).
    -   The decrypted message will be displayed in the GUI.

## ⚠️ Notes & Warnings

-   You can use Python IDLE or Visual Studio Code to execute the scripts.
-   The encrypted image is saved as a `.png` file to preserve the hidden data.
-   **Password Usage:** The password is used as a basic check within the GUI. For robust security, implement advanced cryptographic techniques. The current implementation does not use the password to encrypt the 
  data.
-   **Message Length:** The message length is stored within the encrypted image. Ensure that the image has enough space to store both the message and its length.
-   **Image Size:** Large messages may not fit in small images; use high-resolution images for longer messages.
-   **Error Handling:** The scripts include basic error handling, but additional checks can be added for robustness.
-   **Security Considerations:** Steganography provides a basic level of security. For highly sensitive data, consider using strong encryption methods in conjunction with steganography.
-   **File Integrity:** Avoid modifying the encrypted image using external tools, as this could corrupt the hidden data.

## 📜 License

-   This project is open-source and free to use!
