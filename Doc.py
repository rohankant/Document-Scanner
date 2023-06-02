import re
import pytesseract
from pdf2image import convert_from_path

# Convert the PDF file to images
images = convert_from_path("PdfFile.pdf")

# Scan each image
for image in images:

    # Convert the image to text
    text = pytesseract.image_to_string(image)

    # Split the text into individual words
    words = text.split()

    # Filter the words that are followed by a colon
    filtered_words = re.findall(r'\w+:\s*', text)

    # Join the filtered words into a single string
    output_string = ' '.join(filtered_words)

    # Print the output string
    print(output_string)
