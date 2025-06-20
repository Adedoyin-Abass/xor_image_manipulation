## XOR Image Manipulation
Image Encryption Using Simple Pixel Manipulation

This Python tool offers a straightforward method for encrypting and decrypting images using a simple XOR operation. It's a great example for understanding fundamental image manipulation and cryptographic concepts, though it's not intended for secure encryption of sensitive data.

## Features
* XOR Encryption/Decryption: Applies an XOR operation to each color component (Red, Green, Blue) of every pixel using a user-defined key. Since XOR is its own inverse, the same function can be used for both encryption and decryption.
* Simple Command-Line Interface: Easy-to-use prompts guide you through the process of selecting an image, specifying an output file, and entering a key.
* Handles Common Image Formats: Utilizes the Pillow library to support a wide range of image formats (e.g., PNG, JPG, BMP) by converting them to RGB for consistent processing.

## How it Works
The core of this tool is the xor_encrypt_decrypt function:

* Image Loading: Opens the specified image file and converts it to RGB mode to ensure consistent pixel data (each pixel represented by Red, Green, and Blue values).
* Key Conversion: The provided string key is converted into a sequence of bytes.
* Pixel Iteration: The tool iterates through every pixel in the image.
* XOR Operation: For each pixel's Red, Green, and Blue components, a XOR operation is performed with a corresponding byte from the key. The key bytes are cycled through using the modulo operator to ensure the key is applied repeatedly across the entire image.
* Image Saving: The modified pixel data is then saved as a new image file.
To decrypt an image, you simply rerun the script on the encrypted image using the same key. The XOR operation will reverse the encryption.

## Prerequisites
Before running this tool, you need to have `Python` and the `Pillow library` installed.
* Install `Python3.x`
  * To run this on `Linux`, you should use the script `sudo apt install python3`.
  * To run on `macOS`, install `Homebrew`, then install Python with `brew install python`.
* Pillow Library: You can install it using pip on your terminal: 
Type `pip install Pillow`
Or `py -m pip install Pillow` (if your code editor is returning an error message stating that 'pip' is not recognized as the name of a cmdlet, function, script file, or operable program.)

## Usage
1. Save the Code: Save the provided Python code as a `.py` file (e.g., image_xor.py).
2. Run from Terminal: Open your terminal or command prompt, navigate to the directory where you saved the file, and run the script:
3. Follow the Prompts: The program will guide you through the following steps:

  * Choose to `(E)ncrypt`, `(D)ecrypt`, or `(Q)uit`.
  * Enter the path to your input image file (e.g., my_photo.png).
  * Enter the desired output file name (e.g., encrypted_photo.png or decrypted_photo.png).
  * Provide an encryption/decryption key (any string of characters). Remember this key! You'll need the same key to decrypt the image.
 
 ![Alt text](https://github.com/Adedoyin-Abass/xor_image_manipulation/blob/main/screenshots/Screenshot%202025-06-12%20033427.png)

## Limitations and Security Considerations
* Not for Secure Encryption: This XOR-based method is very basic and offers minimal security. It's susceptible to various cryptanalytic attacks (e.g., frequency analysis, known-plaintext attacks). Do not use this for sensitive or confidential data.
* Key Management: The security heavily relies on the secrecy and strength of the key. A short or easily guessable key provides no protection.
* Simple Transformation: The scrambling effect is purely visual. The underlying data structure remains relatively simple, making it easy to reverse with appropriate tools or knowledge.
This tool is primarily for educational purposes to demonstrate the concept of XOR operations in image processing.

## Contributing
Feel free to fork this repository, make improvements, and submit pull requests. Any contributions are welcome!

## License
This project is open source and available under the MIT License.

## Author
Adedoyin Abass / https://github.com/Adedoyin-Abass
