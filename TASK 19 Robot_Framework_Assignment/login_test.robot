*** Settings ***
Documentation     Robot Framework Login Automation Project
Library           SeleniumLibrary

*** Variables ***
${URL}            https://robotsparebinindustries.com/
${BROWSER}        chrome
${USERNAME}       maria
${PASSWORD}       thoushallnotpass

*** Test Cases ***
Verify Login Functionality
    [Documentation]    This test case verifies successful login and logout functionality.

    # Open browser and maximize window
    Open Application Browser

    # Perform login using valid credentials
    Login To Application

    # Verify successful login
    Verify Successful Login

    # Perform logout operation
    Logout From Application

    # Close browser
    Close Application Browser

*** Keywords ***
Open Application Browser
    [Documentation]    Opens browser and navigates to application URL.

    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    5 seconds

Login To Application
    [Documentation]    Enters username and password then clicks login button.

    Input Text       id:username    ${USERNAME}
    Input Password   id:password    ${PASSWORD}
    Click Button     xpath://button[contains(text(),'Log in')]

Verify Successful Login
    [Documentation]    Verifies that login is successful.

    Wait Until Element Is Visible    xpath://h2[contains(text(),'Orders overview')]    timeout=10 seconds
    Element Should Be Visible        xpath://h2[contains(text(),'Orders overview')]

Logout From Application
    [Documentation]    Logs out from the application.

    Click Button    xpath://button[contains(text(),'Log out')]

Close Application Browser
    [Documentation]    Closes the browser.

    Close Browser
