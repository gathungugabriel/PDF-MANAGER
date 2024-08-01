import sys
import os
import subprocess
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def get_script_path(script_name):
    # Determine base directory based on whether running in a bundled or development environment
    base_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    script_mapping = {
        'script1': 'python_multifolderCARDS_singlecsvextract_pdf_files.py',
        'script2': 'python_multifolderCARDS_combinedcsvextract_pdf_files.py',
        'script3': 'Isiolo_multifolder_combinedcsvextract_pdf_files.py',
        'script4': 'Isiolo_multifolder_individualcsvextract_pdf_files.py',
        'script5': 'extract_parcels_files.py',
        'script6': 'delete_all_csvs.py',
        'script7': 'ocr_renamer.py'
    }
    return os.path.join(base_dir, script_mapping.get(script_name, ''))

def run_script(script_name, root_path, *args):
    script_file = get_script_path(script_name)
    
    if not os.path.exists(script_file):
        raise FileNotFoundError(f"Script file {script_file} does not exist")
    
    # Construct the command to run
    command = ['python', script_file, root_path] + list(args)
    
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout)  # Print script output if needed
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error running script: {e.stderr}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def execute_script():
    script_name = request.form['script']
    root_path = request.form['root_path']
    
    # Check if the specified root path exists
    if not os.path.exists(root_path):
        flash('The specified root path does not exist!', 'danger')
        return redirect(url_for('index'))

    try:
        if script_name == 'script7':
            # Additional user inputs for OCR renamer
            prefix = request.form.get('prefix', '')
            suffix = request.form.get('suffix', '')
            poppler_path = request.form.get('poppler_path', '')
            tesseract_path = request.form.get('tesseract_path', '')
            run_script(script_name, root_path, prefix, suffix, poppler_path, tesseract_path)
        else:
            run_script(script_name, root_path)
        
        flash('Script executed successfully!', 'success')
    except FileNotFoundError as e:
        flash(str(e), 'danger')
    except RuntimeError as e:
        flash(str(e), 'danger')
    except Exception as e:
        flash(f'Unexpected error: {str(e)}', 'danger')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
