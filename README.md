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

## 🔧 Requirements

-   Python 3.x
-   OpenCV (`opencv-python`)

## 📦 Installation

1.  Ensure you have Python 3.x installed.
2.  Install the required library:

    ```bash
    pip install opencv-python
    ```

3.  Clone the repository:

    ```bash
    git clone [https://github.com/ReshmaP-001/Secure-Data-Hiding-In-Images-Using-Steganography.git](https://github.com/ReshmaP-001/Secure-Data-Hiding-In-Images-Using-Steganography.git)
    cd Secure-Data-Hiding-In-Images-Using-Steganography
    ```

## ⚡ Usage

### 🔒 Encrypt a Message into an Image

1.  Run the encryption script:

    ```bash
    python encrypt.py
    ```

2.  Follow the prompts:
    -   Select the image file (supports `.png`, `.jpg`, `.jpeg`).
    -   Enter the secret message to hide.
    -   Set a password for protection.
3.  The encrypted image (`encryptedImage.png`) will be saved in the same directory as the original image.

### 🔑 Decrypt a Hidden Message

1.  Run the decryption script:

    ```bash
    python decrypt.py
    ```

2.  Follow the prompts:
    -   Select the encrypted image file (`encryptedImage.png`).
    -   Enter the correct password.
3.  The decrypted message will be displayed.

## ⚠️ Notes & Warnings

-   You can use Python IDLE or Visual Studio Code to execute the scripts.
-   The encrypted image is saved as a `.png` file to preserve the hidden data.
-   **Password Usage:** The password is used as a basic check within the GUI. For robust security, implement advanced cryptographic techniques. The current implementation does not use the password to encrypt the data.
-   **Message Length:** The message length is stored within the encrypted image. Ensure that the image has enough space to store both the message and its length.
-   **Image Size:** Large messages may not fit in small images; use high-resolution images for longer messages.
-   **Error Handling:** The scripts include basic error handling, but additional checks can be added for robustness.
-   **Security Considerations:** Steganography provides a basic level of security. For highly sensitive data, consider using strong encryption methods in conjunction with steganography.
-   **File Integrity:** Avoid modifying the encrypted image using external tools, as this could corrupt the hidden data.

## Screenshot

![Screenshot 2025-02-25 171230](https://github.com/user-attachments/assets/df20b3bc-d503-4f8c-b6eb-5d075a3769f6)

## 📜 License

-   This project is open-source and free to use!
