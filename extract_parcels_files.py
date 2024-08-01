import os
import csv
import sys

def extract_pdf_files_within_parcels(parcel_path):
    pdf_files = []
    for root, dirs, files in os.walk(parcel_path):
        pdf_files.extend([file for file in files if file.lower().endswith('.pdf')])
    return pdf_files

def save_pdf_files_to_csv(pdf_files, csv_file_path):
    try:
        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['PDF File'])
            for pdf_file in pdf_files:
                file_name = os.path.splitext(pdf_file)[0]
                csv_writer.writerow([file_name])
        print(f"All PDF file names saved to: {csv_file_path}")
    except Exception as e:
        print(f"Error writing to CSV: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_parcels_files.py <root_path>")
        sys.exit(1)

    root_path = sys.argv[1]

    for folder_name in os.listdir(root_path):
        folder_path = os.path.join(root_path, folder_name)
        if os.path.isdir(folder_path):
            pdf_files = extract_pdf_files_within_parcels(folder_path)
            csv_file_name = f"{folder_name}_PARCELS.csv"
            csv_file_path = os.path.join(folder_path, csv_file_name)
            save_pdf_files_to_csv(pdf_files, csv_file_path)
