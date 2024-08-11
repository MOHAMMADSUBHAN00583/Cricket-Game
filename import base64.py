import base64
from PIL import Image
import io

# Read the Base64 string from a file (replace 'base64.txt' with your actual file)
with open('base64.txt', 'rb') as bs64_file:
    bs64_data = bs64_file.read()

# Decode the Base64 string to image data
decoded_img_data = base64.b64decode(bs64_data)

# Create an image from the decoded data
img = Image.open(io.BytesIO(decoded_img_data))

# Save the image as a JPEG file (replace 'output.jpeg' with your desired filename)
img.save('output.jpeg', 'JPEG')

print("Image saved as 'output.jpeg'")
