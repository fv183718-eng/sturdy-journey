import qrcode

def generate_qr_code(url, filename='qrcode.png'):
    """
    Generate a QR code from a given URL and save it as an image file.

    Args:
        url (str): The URL to encode in the QR code.
        filename (str): The name of the output file (default: 'qrcode.png').
    """
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add the URL data to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(filename)
    print(f"QR code saved as {filename}")

if __name__ == "__main__":
    # Example usage
    url = input("Masukkan URL: ")
    filename = input("Masukkan nama file seperti contoh:  'qrcode.png'): ").strip()
    if not filename:
        filename = 'qrcode.png'
    generate_qr_code(url, filename)
