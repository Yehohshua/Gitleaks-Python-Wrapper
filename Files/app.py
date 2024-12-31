import subprocess
import argparse
import os
from pydantic import BaseModel, field_validator
import json

# Define a Pydantic model to structure and validate input data
class GitleaksInput(BaseModel):
    scan_path: str  # Path to the directory to be scanned
    report_path: str  # Path where the report will be saved

    @field_validator("scan_path")
    def check_scan_path(cls, v):
        if not os.path.isdir(v):
            raise ValueError(f"The path {v} is not a valid directory.")
        return v

    @field_validator("report_path")
    def check_report_path(cls, v):
        if not v.endswith(".json"):
            raise ValueError("The report file must end with .json.")
        return v


# Function to run Gitleaks and handle errors
def run_gitleaks(scan_path, report_path):
    command = [
        "docker", "run",  # Run the Docker container
        "-v", f"{scan_path}:/code",  # Mount local directory to container
        "zricethezav/gitleaks:latest",  # Gitleaks Docker image
        "detect",  # Start scan
        "--source", "/code",  # Directory to scan inside container
        "--report-format", "json",  # Output format as JSON
        "--report-path", f"/code/{report_path}",  # Save report inside container
        "--verbose",  # Show detailed output
        "--no-color",  # Disable color in output
        "--no-git"  # Exclude Git-related info
    ]
    
    try:
        result = subprocess.run(command, text=True)
        print(result.stdout)  # Show the output of Gitleaks

        # If there is any error or warning output, display it
        if result.stderr:
            print(f"Error/Warning output: {result.stderr}")
            
    except Exception as e:
        # For any unexpected errors
        error_data = {
            "exit_code": 1,
            "error_message": f"Unexpected error: {str(e)}"
        }
        print_and_save_error(error_data)  # Print and save error as JSON

# Function to write errors to a file and print them
def print_and_save_error(error_data: dict):
    # Print error as JSON to the console
    print(json.dumps(error_data, indent=4))
    
    # Write error to a file
    with open("error_report.json", "w") as f:
        json.dump(error_data, f, indent=4)
        print("Error details have been written to error_report.json")

# Main function 
def main():
    # Define argparse to get scan path and report path from the user
    parser = argparse.ArgumentParser(description='Run Gitleaks scan in Docker')
    parser.add_argument('scan_path', type=str, help='Path to scan directory')
    parser.add_argument('report_path', type=str, help='Path to save the report (e.g. gitleaks_report.json)')
    args = parser.parse_args()

    try:
        # Perform Pydantic validation
        gitleaks_input = GitleaksInput(scan_path=args.scan_path, report_path=args.report_path)
        print(f"Valid input: {gitleaks_input}")

        run_gitleaks(gitleaks_input.scan_path, gitleaks_input.report_path)

    except ValueError as e:
        # If validation fails, handle it and print error as JSON
        error_data = {
            "exit_code": 2,
            "error_message": f"Pydantic validation failed: {str(e)}"
        }
        print_and_save_error(error_data)  # Print and save error as JSON

if __name__ == "__main__":
    main()
