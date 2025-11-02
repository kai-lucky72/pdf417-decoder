from PIL import Image as PIL
from pdf417decoder import PDF417Decoder
import sys
import os

# Define the path to your image file
# NOTE: Replace 'image_3481a8.jpg' with the actual path to your saved image
image_path = 'image_3481a8.jpg'

if not os.path.exists(image_path):
    print(f"Error: Image file not found at {image_path}")
    sys.exit(1)

try:
    # Open the image using Pillow
    image = PIL.open(image_path)

    # Initialize the decoder
    decoder = PDF417Decoder(image)

    # Attempt to decode the barcode
    if decoder.decode() > 0:
        # Get the decoded text from the first (and usually only) barcode found
        decoded_data = decoder.barcode_data_index_to_string(0)

        print("✅ **Decoded PDF417 Data:**")
        print("---")
        print(decoded_data)
        print("---")
    else:
        print("❌ Could not decode the PDF417 barcode. Ensure the image is clear and the barcode is cropped accurately.")

except Exception as e:
    print(f"An error occurred during decoding: {e}")