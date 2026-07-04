# Email Domain Updater

A Python utility that reads employee records from a CSV file, finds email addresses belonging to a specific domain, replaces them with a new domain, and generates an updated CSV report.

## Overview

This project demonstrates:

* File handling with Python
* CSV data processing
* Regular expressions (Regex)
* Data transformation and reporting
* Basic automation scripting

The script scans a CSV file containing employee information, identifies email addresses using a specified domain, updates them to a new domain, and saves the results in a separate CSV file.

---

## Features

* Read employee records from a CSV file
* Detect email addresses belonging to a specific domain
* Replace an old domain with a new domain
* Generate a new CSV report without modifying the original file
* Simple and easy-to-customize code
* Uses Python standard libraries only (no external dependencies)

---

## Project Structure

```text
email-domain-updater/
│
├── update_emails.py
├── user_emails.csv
├── updated_user_emails.csv   # Generated after execution
└── README.md
```

---

## Requirements

* Python 3.6 or higher

Verify your Python installation:

```bash
python3 --version
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/saimamustafa-520/email-domain-updater.git
```

Move into the project directory:

```bash
cd email-domain-updater
```

---

## CSV Format

The input CSV file should follow this structure:

```csv
Full Name,Email Address,Department
Alice Johnson,alice.johnson@abc.edu,Human Resources
Bob Smith,bob.smith@abc.edu,IT
Charlie Brown,charlie.brown@xyz.edu,Finance
```

---

## Configuration

Open `update_emails.py` and modify the domains if needed:

```python
old_domain = "abc.edu"
new_domain = "xyz.edu"
```

---

## Running the Script

Execute:

```bash
python3 update_emails.py
```

Example output:

```text
Updated file created: updated_user_emails.csv
```

---

## Example

### Before

```csv
Alice Johnson,alice.johnson@abc.edu,Human Resources
Bob Smith,bob.smith@abc.edu,IT
Charlie Brown,charlie.brown@xyz.edu,Finance
```

### After

```csv
Alice Johnson,alice.johnson@xyz.edu,Human Resources
Bob Smith,bob.smith@xyz.edu,IT
Charlie Brown,charlie.brown@xyz.edu,Finance
```

---

## How It Works

1. Reads employee records from the CSV file.
2. Identifies email addresses belonging to the old domain.
3. Replaces the old domain with the new domain using regular expressions.
4. Writes the updated records to a new CSV file.
5. Preserves the original input file.

---

## Technologies Used

* Python 3
* CSV Module
* Regular Expressions (`re`)

---

## Learning Objectives

This project is useful for practicing:

* Python scripting
* CSV file manipulation
* Regex pattern matching
* Data processing automation
* Git and GitHub workflows

---

## Future Improvements

* Command-line arguments for custom domains
* Support for multiple domain replacements
* Logging and error handling
* Interactive user input
* Unit tests

---

## Author
* Saima Mustafa


