# -*- mode: python ; coding: utf-8 -*-
import os
from PyInstaller.utils.hooks import collect_submodules

# Set the base directory to the current directory of the .spec file
base_dir = os.getcwd()

# Manually specify the hidden imports
hidden_imports = collect_submodules('flask') + collect_submodules('pytesseract') + collect_submodules('pdf2image')

a = Analysis(
    ['app.py'],
    pathex=[base_dir],
    binaries=[],
    datas=[
        ('templates', 'templates'),  # Template files
        ('delete_all_csvs.py', '.'), # Additional script files
        ('extract_parcels_files.py', '.'),
        ('Isiolo_multifolder_combinedcsvextract_pdf_files.py', '.'),
        ('Isiolo_multifolder_individualcsvextract_pdf_files.py', '.'),
        ('ocr_renamer.py', '.'),
        ('python_multifolderCARDS_combinedcsvextract_pdf_files.py', '.'),
        ('python_multifolderCARDS_singlecsvextract_pdf_files.py', '.'),
    ],
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
