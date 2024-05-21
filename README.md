# Playwright Assignment

This project is a demonstration of automated testing using Playwright for testing Gmail functionalities.

## Overview

The goal of this assignment is to automate the testing of various Gmail functionalities such as login and sending emails.

## Features

- Automated login to Gmail - 4 testcases from assigment block1
- Composing and sending email with attachment - 1 testcase from assigment block3


## Technologies Used

- **Playwright**: Playwright is a powerful automation library that allows us to automate interactions with web pages in various browsers.
- **Pytest**: Pytest is a testing framework that makes it easy to write simple and scalable tests in Python.
- **Pytest-bdd**: Pytest-bdd is a plugin for pytest that enables Behavior-Driven Development (BDD) style testing using Gherkin syntax.
- **Python**: Python is the programming language used for writing the test automation code.

## Project Structure

The project is organized as follows:

PlaywrightAssignment/

│
 
├── features/

│   ├── email.feature

│   └── login.feature

│

├── pageObjects/

│   ├── __init__.py

│   ├── emailPageObjects.py

│   └── loginPageObjects.py

│

├── steps/

│   ├── __init__.py

│   ├── test_email.py

│   └── test_login.py

│

├── smile.jpg

│

└── README.md

