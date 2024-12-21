from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
   
    img = Image.open(input_path)
    img_array = np.array(img, dtype=np.int32) 
    encrypted_array = (img_array + key) % 256

    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")


def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img_array = np.array(img, dtype=np.int32) 

    decrypted_array = (img_array - key) % 256
    decrypted_array = decrypted_array % 256

    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Simple Image Encryption Tool")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode: encrypt or decrypt")
    parser.add_argument("input", help="Path to the input image")
    parser.add_argument("output", help="Path to save the output image")
    parser.add_argument("key", type=int, help="Encryption/Decryption key (integer)")

    args = parser.parse_args()

    if args.mode == "encrypt":
        encrypt_image(args.input, args.output, args.key)
    elif args.mode == "decrypt":
        decrypt_image(args.input, args.output, args.key)
