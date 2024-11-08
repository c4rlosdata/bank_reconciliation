# Bank Reconciliation Automation Project

This project is a **Bank Reconciliation Automation System** developed in Python. It standardizes and reconciles financial transactions between an accounting file (generated for bookkeeping) and the company's internal financial report (from their financial system). The system uses Excel files as input, formats them, and automatically cross-checks and fills discrepancies, saving significant manual effort.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Requirements](#requirements)
5. [Installation](#installation)
6. [Usage](#usage)
7. [How It Works](#how-it-works)
8. [Customization](#customization)
9. [Troubleshooting](#troubleshooting)
10. [Future Improvements](#future-improvements)
11. [License](#license)

---

## Project Overview
This system:
- Reads two Excel files: one from the bank (Itaú) and another from the company (Kazah).
- Formats the data from both files.
- Reconciles financial transactions by matching amounts directly or through combinations.
- Generates a unified, reconciled Excel report, detailing all matched and unmatched transactions.

## Features
- **Automated Formatting**: Formats input Excel files, making them uniform for analysis.
- **Transaction Matching**: Matches transactions based on value and identifies discrepancies between the files.
- **Combination Matching**: Searches for combinations of transactions (up to four entries) to match outstanding values.
- **Detailed Output**: Produces a final Excel report with matched entries and descriptive fields for easier review.

## Project Structure
The project consists of three main Python files:
- `main_script.py`: The GUI-driven main application file that allows users to select and process the files.
- `formatacao.py`: Contains the `format_files` function for cleaning and formatting the raw Excel files.
- `preenchedor_v2.py`: Handles the reconciliation logic, filling in descriptions and matching transactions.

### Folder Layout
```
├── main_script.py            # Main GUI script to run the project
├── formatacao.py             # File for data formatting functions
├── preenchedor_v2.py         # File for reconciliation and matching functions
├── requirements.txt          # List of Python dependencies
```

## Requirements
- Python 3.8+
- Dependencies:
  - `pandas` (data manipulation)
  - `numpy` (numeric operations)
  - `tkinter` (GUI for user interactions)

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/bank-reconciliation-automation.git
   cd bank-reconciliation-automation
   ```
2. Install the required Python libraries.

## Usage
1. **Run the GUI Application**: Open the main script to launch the interface.
   ```bash
   python main_script.py
   ```
2. **Select Files**: Choose the two Excel files (one from Itaú, one from Kazah) when prompted by the interface.
3. **Process Files**: The script will automatically format the data, reconcile transactions, and save the results in a file named `planilha_principal_v2.xlsx` in the project directory.

## How It Works
1. **File Formatting**:
   - `format_files` function in `formatacao.py` processes the Itaú and Kazah Excel files, reformatting columns and removing unnecessary data.
2. **Transaction Reconciliation**:
   - The `sheet_filling` function in `preenchedor_v2.py` performs transaction matching. It attempts to match each transaction in the Itaú file with one or more entries from the Kazah file.
   - The function supports combination matching (up to 4 entries) to resolve complex cases.
3. **Output Generation**:
   - Once reconciled, the final Excel report is generated, displaying all matched entries and leaving unmatched values for further review.

## Customization
- **File Paths**: Modify file paths in the `main_script.py` to set custom directories if needed.
- **Matching Criteria**: Update criteria in `preenchedor_v2.py` to match specific reconciliation requirements, such as custom tolerance thresholds for value matching.

## Troubleshooting
- **File Not Found**: Ensure the selected files are valid Excel files.
- **Unmatched Transactions**: Review the final report to identify any missing transactions; you may need to refine the matching criteria.
- **Formatting Errors**: Ensure the input files match the expected format (Itaú and Kazah Excel files).

## Future Improvements
- **Automated Scheduling**: Implement periodic reconciliation via a task scheduler.
- **Enhanced GUI**: Expand the interface to support additional configuration options.
- **Dynamic Matching Logic**: Enable configurable matching tolerances and thresholds for more flexibility.

## License
This project is licensed under the MIT License.

