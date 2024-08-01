import os
import cv2
import re
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
from pytesseract import image_to_string, pytesseract
from pdf2image import convert_from_path
from pdf2image.exceptions import PDFPageCountError
import sys

# Function to enhance image contrast
def enhance_image(image, contrast_factor):
    img_array = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    img_array = cv2.convertScaleAbs(img_array, alpha=contrast_factor, beta=0)
    enhanced_image = Image.fromarray(cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB))
    sharpened_image = enhanced_image.filter(ImageFilter.SHARPEN)
    return sharpened_image

# Function to convert PDF to images
def convert_pdf_to_img(pdf_file, poppler_path):
    try:
        return convert_from_path(pdf_file, poppler_path=poppler_path)
    except PDFPageCountError as e:
        print(f"Error converting PDF to images: {e}")
        return []

# Function to extract text from image
def convert_image_to_text(image):
    return image_to_string(image)

# Function to extract parcel number from text
def extract_parcel_number(text):
    parcel_number = re.search(r'PARCEL NUMBER\s*(\d+)', text)
    return parcel_number.group(1) if parcel_number else None

# Function to process PDF, enhance images, and extract parcel number
def process_pdf_and_rename(pdf_file, poppler_path, tesseract_path, prefix, suffix, counter):
    contrast_factor = 1.1
    max_contrast_factor = 2.0

    while contrast_factor <= max_contrast_factor:
        images = convert_pdf_to_img(pdf_file, poppler_path)
        final_text = ''

        for pg, img in enumerate(images):
            enhanced_img = enhance_image(img, contrast_factor)
            text = convert_image_to_text(enhanced_img)
            final_text += text

            parcel_number = extract_parcel_number(text)
            if parcel_number:
                break

        if parcel_number:
            break
        else:
            contrast_factor += 0.2

    # Use the parcel number if found; otherwise, generate a counter-based name
    new_name = f'{prefix}_{parcel_number}' if parcel_number else f'{prefix}_{suffix}_{counter}'

    # Check if the destination file already exists
    destination_path = os.path.join(root, f'{new_name}.pdf')
    if not os.path.exists(destination_path):
        # Rename the PDF file using the new name
        os.rename(pdf_file, destination_path)
        print(f"Renamed PDF to: {new_name}.pdf")
    else:
        print(f"Skipped renaming. File with name {new_name}.pdf already exists.")
    return final_text, new_name

if __name__ == "__main__":
    # Ensure the necessary arguments are passed
    if len(sys.argv) != 5:
        print("Usage: python ocr_renamer.py <folder_path> <prefix> <suffix> <poppler_path> <tesseract_path>")
        sys.exit(1)

    # Get the command-line arguments
    folder_path = sys.argv[1]
    prefix = sys.argv[2]
    suffix = sys.argv[3]
    poppler_path = sys.argv[4]
    tesseract_path = sys.argv[5]

    # Set the Tesseract executable path
    pytesseract.tesseract_cmd = tesseract_path

    # Check if the specified folder path exists
    if os.path.exists(folder_path):
        # Run the PDF renaming code
        for root, dirs, files in os.walk(folder_path):
            counter = 1  # Initialize the counter
            for pdf_file in [f for f in files if f.lower().endswith('.pdf')]:
                full_pdf_path = os.path.join(root, pdf_file)
                try:
                    extracted_text, new_name = process_pdf_and_rename(full_pdf_path, poppler_path, tesseract_path, prefix, suffix, counter)

                    # Print extracted text for reference
                    print("Extracted Text:")
                    print(extracted_text)

                    # Increment the counter for the next iteration
                    counter += 1
                except Exception as e:
                    print(f"Error processing PDF file '{pdf_file}': {e}")
    else:
        print(f"The specified folder path does not exist: {folder_path}")
