# OrangeHRM Automation Testing Project

## Project Description
This project automates the OrangeHRM web application using Selenium WebDriver with Python and PyTest framework.

Application URL:
https://opensource-demo.orangehrmlive.com

---

# Technologies Used

- Python
- Selenium WebDriver
- PyTest
- WebDriver Manager
- HTML Reports

---

# Features Covered

- Valid Login Test
- Invalid Login Test
- Login Field Validation
- Dashboard Menu Validation
- Forgot Password Validation
- My Info Validation
- Leave Module Validation
- User Creation Validation
- Claim Section Validation

---

# Project Structure

orangehrm_project/
│
├── all_tests.py
├── requirements.txt
├── pytest.ini
├── README.md
├── reports/
│
├── tests/
│   ├── test_login.py
│   ├── test_dashboard.py
│   ├── test_leave.py
│   ├── test_claim.py
│   └── test_user_management.py
│
├── utilities/
│   ├── config.py
│   └── driver_setup.py
│
└── test_cases.xlsx

---

# Installation

Install required libraries:

pip install -r requirements.txt

---

# Run Tests

Run complete project:

pytest

Run single file:

pytest tests/test_login.py

---

# Generate HTML Report

pytest --html=reports/report.html --self-contained-html

---

# Author

Automation Testing Assignment