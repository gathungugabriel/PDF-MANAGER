import os
import csv
import sys

def extract_last_two_subfolders(folder_path):
    """Extract the last two components of a folder path."""
    folder_components = folder_path.split(os.sep)
    return folder_components[-2], folder_components[-1]

def extract_pdf_folders_within_parcels(parcel_path):
    """Extract all PDF folders within the given path."""
    pdf_folders = []

    for root, dirs, files in os.walk(parcel_path):
        pdf_files = [f for f in files if f.lower().endswith('.pdf')]
        if pdf_files:
            location, parcel = extract_last_two_subfolders(root)
            pdf_folders.append((location, parcel))

    return pdf_folders

def save_pdf_folders_to_csv(pdf_folders, csv_file_path):
    """Save the PDF folders to a CSV file."""
    try:
        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Location', 'Parcel'])
            for location, parcel in pdf_folders:
                csv_writer.writerow([location, parcel])
        return f"All PDF folder names saved to: {csv_file_path}"
    except Exception as e:
        return f"Error writing to CSV: {str(e)}"

def process_pdf_folders(root_path):
    """Process the PDF folders and save them to a CSV file."""
    results = []

    for root, dirs, files in os.walk(root_path):
        for folder in dirs:
            subfolder_path = os.path.join(root, folder)
            pdf_folders = extract_pdf_folders_within_parcels(subfolder_path)

            if pdf_folders:
                parent_folder_name, _ = extract_last_two_subfolders(subfolder_path)
                immediate_subfolder_name = folder
                csv_file_name = f"{parent_folder_name}_{immediate_subfolder_name}_PARCELS.csv"
                csv_file_path = os.path.join(subfolder_path, csv_file_name)
                result = save_pdf_folders_to_csv(pdf_folders, csv_file_path)
                results.append(result)
            else:
                results.append(f"No PDF files found in the subfolders of: {subfolder_path}")

    return results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python Isiolo_multifolder_individualcsvextract_pdf_files.py <root_path>")
        sys.exit(1)

    root_path = sys.argv[1]
    if not os.path.exists(root_path):
        print(f"The specified root path does not exist: {root_path}")
        sys.exit(1)

    results = process_pdf_folders(root_path)
    for result in results:
        print(result)
