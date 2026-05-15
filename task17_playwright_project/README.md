# Task 17 - Playwright + Pytest Automation Framework

## Technologies Used
- Python
- Microsoft Playwright
- Pytest
- Pytest HTML Report

## Framework Features
- Page Object Model (POM)
- Explicit Waits
- OOPS Concepts
- Exception Handling
- HTML Reports

## Test Scenarios
1. Successful Login
2. Unsuccessful Login
3. Validate Username Input Box
4. Validate Password Input Box
5. Validate Submit Button
6. Validate Logout Functionality

## Installation
```bash
pip install -r requirements.txt
playwright install
```

## Run Tests
```bash
pytest tests/test_login.py --html=reports/report.html
```

## Project Structure
task17_playwright_project/
│
├── pages/
│   └── login_page.py
│
├── tests/
│   └── test_login.py
│
├── reports/
│
├── requirements.txt
├── pytest.ini
└── README.md
