import os
import sys

def delete_csv_files(root_path):
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if file.lower().endswith('.csv'):
                try:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    print(f"Deleted CSV file: {file_path}")
                except Exception as e:
                    print(f"Error deleting CSV file: {str(e)}")

if __name__ == "__main__":
    # Ensure the root path is passed as an argument
    if len(sys.argv) != 2:
        print("Usage: python delete_all_csvs.py <root_path>")
        sys.exit(1)

    # Get the root path from command-line arguments
    root_path = sys.argv[1]

    # Delete all CSV files within subfolders of the root path
    delete_csv_files(root_path)
