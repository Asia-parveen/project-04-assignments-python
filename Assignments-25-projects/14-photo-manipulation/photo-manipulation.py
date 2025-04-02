from PIL import Image, ImageEnhance, ImageFilter

# Function to adjust brightness of an image
def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

# Function to adjust contrast of an image
def adjust_contrast(image, factor):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

# Function to apply blur on an image
def apply_blur(image, radius):
    return image.filter(ImageFilter.GaussianBlur(radius))

# Load an image
image_path = "book.jpg"  # Replace with your image path
image = Image.open(image_path)

# Display original image
image.show()

# Apply brightness adjustment
brightness_factor = 1.5  # Increase brightness by 1.5 times
bright_image = adjust_brightness(image, brightness_factor)
bright_image.show()

# Apply contrast adjustment
contrast_factor = 2.0  # Increase contrast by 2 times
contrast_image = adjust_contrast(image, contrast_factor)
contrast_image.show()

# Apply blur
blurred_image = apply_blur(image, 5)  # Apply Gaussian blur with radius 5
blurred_image.show()

# Save the manipulated images
bright_image.save("bright_image.jpg")
contrast_image.save("contrast_image.jpg")
blurred_image.save("blurred_image.jpg")
