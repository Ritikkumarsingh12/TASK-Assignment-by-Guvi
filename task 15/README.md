# OrangeHRM Data Driven Testing Framework

## Technologies Used
- Selenium
- Python
- Pytest
- Openpyxl
- POM (Page Object Model)
- DDTF (Data Driven Testing Framework)

## Run the Project

Install dependencies:

pip install -r requirements.txt

Run the test:

pytest -v --html=report.html

## Features
- Uses Excel for test data
- Reads 5 username/password combinations
- Writes Pass/Fail result back into Excel
- Uses Explicit Wait
- Uses Pytest HTML report
- Uses POM framework
- No sleep() used