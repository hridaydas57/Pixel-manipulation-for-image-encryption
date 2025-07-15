# prodigy_task02

from PIL import Image

def encrypt_image(image_path, key, output_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            # XOR each channel with key
            pixels[i, j] = (r ^ key, g ^ key, b ^ key)

    img.save(output_path)
    print(f"Encrypted image saved to {output_path}")


def decrypt_image(image_path, key, output_path):
    # Decryption is same as encryption with XOR
    encrypt_image(image_path, key, output_path)


def main():
    print(" Image Encryption Tool")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Enter your choice (1 or 2): ")

    image_path = input("Enter the path to the image: ")
    key = int(input("Enter a numeric key (0–255): "))
    output_path = input("Enter the output image file name (with .png/.jpg): ")

    if choice == '1':
        encrypt_image(image_path, key, output_path)
    elif choice == '2':
        decrypt_image(image_path, key, output_path)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
