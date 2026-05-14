# Task 18 - Python BDD Behave Framework with Allure Report

## Framework Used
- Python Selenium
- Behave BDD Framework
- Allure Reporting
- Page Object Model (POM)
- OOPS Concepts
- Selenium Exceptions

## Features Included
- Successful Login Validation
- Unsuccessful Login Validation
- Username Field Validation
- Password Field Validation
- Logout Validation

## Run Commands

Install dependencies:

pip install -r requirements.txt

Run Behave Tests:

behave

Generate Allure JSON Results:

behave -f allure_behave.formatter:AllureFormatter -o reports/

Generate HTML Report:

allure serve reports/

## Project Structure
- features/
- step_definitions/
- pages/
- reports/