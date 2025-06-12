from PIL import Image
import os

def xor_encrypt_decrypt(image_path, output_path, key):
    try:
        # Open the image
        img = Image.open(image_path)
        # Convert image to RGB if it's not already (e.g., grayscale, RGBA)
        # This ensures consistent pixel structure (R, G, B tuples)
        if img.mode != 'RGB':
            img = img.convert('RGB')

        width, height = img.size
        pixels = img.load() # Load pixel data for direct manipulation

        key_bytes = key.encode('utf-8') # Convert key string to bytes
        key_len = len(key_bytes)

        if not key_len: # Added check for empty key
            print("Error: The key cannot be empty.")
            return

        print(f"Processing image: {image_path}...")

        # Iterate over each pixel
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y] # Get current RGB values

                # Apply XOR operation to each color component
                # Use modulo operator to cycle through the key bytes
                r_new = r ^ key_bytes[(x * 3 + y * width * 3 + 0) % key_len]
                g_new = g ^ key_bytes[(x * 3 + y * width * 3 + 1) % key_len]
                b_new = b ^ key_bytes[(x * 3 + y * width * 3 + 2) % key_len]

                # Update the pixel with the new values
                pixels[x, y] = (r_new, g_new, b_new)

        # Save the processed image
        img.save(output_path)
        print(f"Successfully processed image saved to: {output_path}")

    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Image Encryption/Decryption Tool")
    print("This tool uses a basic XOR operation on pixel values, resulting in a visually scrambled image.")

    while True:
        # Ask if the user wants to encrypt, decrypt, or exit
        while True:
            choice = input("\nDo you want to (E)ncrypt, (D)ecrypt, or (Q)uit? (E/D/Q): ").strip().upper()
            if choice in ['E', 'D', 'Q']:
                break
            else:
                print("Invalid choice. Please enter 'E' for Encrypt, 'D' for Decrypt, or 'Q' to Quit.")

        if choice == 'Q':
            print("Exiting Image Encryption/Decryption Tool. Goodbye!")
            break # Exit the main loop and thus the program

        input_file = input("Enter the path to the input image file (e.g., image.png): ").strip()
        output_file = input("Enter the desired output file name (e.g., processed_image.png): ").strip()
        encryption_key = input("Enter the encryption/decryption key (any string): ").strip()

        if not encryption_key:
            print("Error: The key cannot be empty. Please provide a key.")
            # We don't 'return' here, we just let the loop continue for the next iteration
            continue # Skip to the next iteration of the outer loop

        # Use the same function for both encryption and decryption
        xor_encrypt_decrypt(input_file, output_file, encryption_key)

if __name__ == "__main__":
    main()