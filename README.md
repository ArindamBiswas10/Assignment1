# Assignment1
# Employee Data Transformation Project

## Overview

This project involves transforming employee data from a columnar format into a structured historical, row-based versioning format. The Python script provided in this repository takes an input CSV file containing employee data and processes it to create a format suitable for database storage. The transformed data is aimed at facilitating historical data analysis, including fields for employee identifiers, compensation, dates, performance ratings, and engagement scores.

## Project Structure

- **`exercise1.py`**: The Python script responsible for transforming the input data.
- **`input.csv`**: Sample input CSV file containing employee data.
- **`output.csv`**: The resulting CSV file after applying the data transformation.

## Task Instructions

### Effective and End Dates

- Derive 'Effective Date' and 'End Date' for each historical record.
- Ensure the 'End Date' is one day before the next 'Effective Date' to avoid overlap.
- For the latest record of an employee, assign a far-future date (e.g., 2100-01-01) as the 'End Date'.

### Data Transformation

- Transform columnar data related to compensation, engagement, and review into a row-based format.
- Each row should represent a specific period with consistent data.
- If data for a range is missing, inherit values from the most recent past record for the same employee.

### Data Copying

- Maintain unchanged values for fields without associated dates across different records.
- Ensure all relevant data from the input file is accurately reflected in the output format.

## Usage

1. Ensure you have Python installed on your machine.
2. Clone this repository:

   ```bash
   git clone <https://github.com/ArindamBiswas10/Assignment1.git>
