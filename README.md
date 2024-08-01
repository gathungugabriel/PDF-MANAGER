# About PDF Manager

## Overview

PDF Manager is a versatile application designed to help you manage and process PDF files through a user-friendly web interface. It allows you to run various Python scripts for tasks such as extracting information from PDFs, deleting files, and more. The application is built with Flask and leverages Bootstrap for a responsive and intuitive user experience.

## Features

- **Script Selection**: Easily choose from a list of pre-defined Python scripts.
- **Root Path Input**: Provide the root path for the script to operate on.
- **Dynamic Input Forms**: For scripts requiring additional parameters (e.g., OCR Renamer).
- **Flash Messages**: Get immediate feedback on script execution status, with messages that disappear after 3 seconds.
- **Bootstrap Integration**: Enjoy a clean, responsive interface.

## Getting Started

### Installation

#### Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/gathungugabriel/PDF-MANAGER.git
Navigate to the project directory:

bash
Copy code
cd pdf-manager
Install Python
Download the Python 3.12.4 executable for your operating system from the official Python website.

Run the installer and ensure you check the "Add Python to PATH" option during installation. This will allow you to run Python and pip commands from the command line.

Set Up a Virtual Environment
Create a virtual environment to manage dependencies:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS/Linux:

bash
Copy code
source venv/bin/activate
Install Required Packages
Install the necessary Python packages using pip:

bash
Copy code
pip install -r requirements.txt
Running the Application
Start the Flask Development Server:

Run the application with:

bash
Copy code
python app.py
Open your web browser and go to http://127.0.0.1:5000 to access the application.

Usage
Select a Script: Choose the script you want to run from the dropdown menu.
Enter Root Path: Provide the root path where the script will operate.
Additional Parameters: For scripts like OCR Renamer, enter the required additional parameters.
Run Script: Click the "Run Script" button to execute the selected script.
View Flash Messages: Check the feedback on script execution status, which will disappear after 3 seconds.
Supported Scripts
The application supports the following scripts:

Extract Cards: Extracts cards from a specified folder.
Extract Combined Cards Folders: Extracts combined folders for cards.
Extract Combined Parcels Folders: Extracts combined folders for parcels.
Extract Parcels: Extracts parcel information.
Delete All CSVs: Deletes all CSV files in the specified directory.
OCR Renamer: Renames files using OCR with customizable prefix, suffix, and paths for Poppler and Tesseract.
Contributing
Contributions to PDF Manager are welcome! To contribute:

Fork the repository.

Create a new branch for your changes:

bash
Copy code
git checkout -b feature/your-feature
Make your changes and commit them:

bash
Copy code
git commit -am 'Add new feature'
Push to your branch:

bash
Copy code
git push origin feature/your-feature
Create a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For questions or support:

Email: generalgab630@gmail.com
GitHub Issues: Submit an issue
