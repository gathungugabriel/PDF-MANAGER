import os
import csv
import sys

def extract_last_two_subfolders(folder_path):
    # Split the path into components and return the last two components
    folder_components = folder_path.split(os.sep)
    return folder_components[-2], folder_components[-1]

def extract_pdf_folders_within_parcels(parcel_path):
    pdf_folders = []

    # Walk through the subfolders of the "PARCELS" folder
    for root, dirs, files in os.walk(parcel_path):
        # Filter PDF files
        pdf_files = [f for f in files if f.lower().endswith('.pdf')]

        if pdf_files:
            # Extract the last two subfolder names
            location, parcel = extract_last_two_subfolders(root)
            pdf_folders.append((location, parcel))

    return pdf_folders

def save_pdf_folders_to_csv(pdf_folders, csv_file_path):
    try:
        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Location', 'Parcel'])

            for location, parcel in pdf_folders:
                csv_writer.writerow([location, parcel])

        print(f"All PDF folder names saved to: {csv_file_path}")
    except Exception as e:
        print(f"Error writing to CSV: {str(e)}")

def main(root_path):
    # Initialize list to accumulate PDF folder names
    all_pdf_folders = []

    # Recursively traverse all subfolders within the root path
    for root, dirs, files in os.walk(root_path):
        for folder in dirs:
            subfolder_path = os.path.join(root, folder)
            
            # Extract the PDF folders within each subfolder
            pdf_folders = extract_pdf_folders_within_parcels(subfolder_path)

            if pdf_folders:
                # Append PDF folder names to the list
                all_pdf_folders.extend(pdf_folders)  
            else:
                print(f"No PDF files found in the subfolders of the specified folder: {subfolder_path}")

    # Generate the CSV file name dynamically based on the root folder name
    root_folder_name = os.path.basename(root_path)
    csv_file_name = f"{root_folder_name}_PARCELS.csv"

    # Save all PDF folder names to a single CSV file with the dynamically generated name
    csv_file_path = os.path.join(root_path, csv_file_name)
    save_pdf_folders_to_csv(all_pdf_folders, csv_file_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python Isiolo_multifolder_combinedcsvextract_pdf_files.py <root_path>")
        sys.exit(1)

    root_path = sys.argv[1]
    if not os.path.exists(root_path):
        print(f"The specified root path does not exist: {root_path}")
        sys.exit(1)

    main(root_path)
