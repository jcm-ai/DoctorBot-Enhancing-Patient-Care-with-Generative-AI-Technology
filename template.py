import os
from pathlib import Path
import logging

# Configure logging settings
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# List of files to be created
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py"
    "app.py",
    "research/trials.ipynb",
    "test.py"
]

# Iterate through the list of files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directory if it doesn't exist
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create an empty file if it doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
