# Gitleaks Python Wrapper

Developed by Yehoshua Kasaon

### Introduction

This project is a Python wrapper for Gitleaks, designed to help you scan directories for secrets and vulnerabilities using Docker.

### Setup Instructions

1. Ensure you have the following files in your directory:
   - `Dockerfile`
   - `app.py`
   - `requirements.txt`
2. Enter the folder "Files" and copy these files into the directory you want to scan using Gitleaks.
3. Open a terminal in the directory.
4. Build the Docker image by running:
   ```bash
   docker build -t gitleaks-python-wrapper .
   ```
5. Run the Python script with the following command:
   ```bash
   python app.py "PATH_TO_YOUR_DIRECTORY" "gitleaks_report.json"
   ```
   Replace **`"PATH_TO_YOUR_DIRECTORY"`** with the path of the directory you wish to scan.

### Notes

- Make sure Docker is installed and running on your system before proceeding.
- Ensure Python is installed and added to the system PATH.
- Ensure the directory you want to scan is accessible and has the necessary permissions.
- The script will create a JSON report in the specified directory containing the scan results.
- If any validation errors occur (e.g., invalid paths), they will be displayed and logged in a file.
- The execution steps described above are tested and verified on Windows operating systems.
- **Note:** If Pydantic is not working after building the Docker on a Windows system, run the following command:
   ```bash
   pip install pydantic
   ```

### Additional Resources

- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/) - Used for data validation and management in Python.
- [Docker Official Documentation](https://docs.docker.com/get-started/) - For practicing Docker concepts and commands.
- [Gitleaks GitHub Repository](https://github.com/zricethezav/gitleaks) - The main tool utilized for scanning secrets.
- [Python OS Module Documentation](https://docs.python.org/3/library/os.html) - Used for path and directory handling.
