import qrcode
import cv2

def generate_qr(data, filename="qrcode.png"):
    """Generate a QR code from the given data and save it as an image."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"QR Code saved as {filename}")

def decode_qr(image_path):
    """Decode the QR code from the given image file."""
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(img)
    if data:
        print(f"Decoded Data: {data}")
    else:
        print("No QR Code found!")

if __name__ == "__main__":
    # Example usage
    text = input("Enter the text or URL to encode: ")
    generate_qr(text, "my_qr.png")
    decode_qr("my_qr.png")
