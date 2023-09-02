# Features to Excel
Convert Gherkin feature files into Excel files seamlessly.

## Description
This tool allows users to parse Gherkin feature files and export the parsed data to Excel spreadsheets. It's designed to facilitate easier reading and sharing of feature definitions with non-technical stakeholders. It is built in Python and leverages the power of PyInstaller to create standalone executables.

## Features
Recursive Directory Parsing: Easily find and process all feature files in a directory and its subdirectories.
Excel Sheet Formatting: Customize the structure and appearance of the generated Excel sheets based on a provided configuration.
Configurable Directory Structure: Define how your directory structure should be reflected in the Excel output.
Validation Step Parsing: Use the provided parsing utility to match and extract data from the steps in the feature files.
Prerequisites
Ensure you have Python (3.7 or higher) installed on your machine.

## Setup & Installation

Clone the repository:
```ps1
git clone [repository_url]
```

Navigate to the directory:
```ps1
cd features-to-excel
```

It's recommended to create a virtual environment for the project to keep dependencies isolated. To set up a virtual environment named .venv in the current directory:
```ps1
python -m venv .venv
```

After creating the virtual environment, you need to activate it:
- Windows:
  ```ps1
  .\.venv\Scripts\Activate
  ```

- macOS and Linux:
  ```sh
  source .venv/bin/activate
  ```

Install the necessary dependencies:
```ps1
pip install -r requirements.txt
```

Build the standalone executable (if required):
```ps1
./build.ps1
```

## Usage
Once installed, you can use the tool as follows:

```ps1
python main.py
```

Alternatively, if you built the standalone executable, double click or run:

```ps1
./release/features_to_excel.exe
```

## Troubleshooting
If you encounter issues related to missing files when using the standalone executable, ensure that all the necessary data files (e.g., gherkin-languages.json) are packaged correctly during the build process. Refer to the build script and PyInstaller documentation for more details.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
