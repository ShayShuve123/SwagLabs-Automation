# SwagLabs Automation

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/) [![Selenium](https://img.shields.io/badge/Selenium-4.10.0-green)](https://www.selenium.dev/) [![Pytest](https://img.shields.io/badge/Pytest-7.3.1-brightgreen)](https://docs.pytest.org/en/stable/)

## Project Overview
SwagLabs Automation is an automated testing framework designed for the SwagLabs website using Selenium and Pytest. The framework automates testing for both the Login and Home pages and generates a detailed HTML report of the test results.

## Features
- **Login Page Testing:** Validates both successful and failed login scenarios.
- **Home Page Testing:** Identifies and adds the cheapest product to the shopping cart.
- **HTML Reporting:** Produces a comprehensive HTML report using Pytest-HTML.
- **Jenkins Integration:** Easily integrates with Jenkins for continuous integration and automated testing.

## Prerequisites
- **Python 3.11** (or a compatible version)
- **Google Chrome** must be installed on your system.
- **ChromeDriver:** Ensure that the ChromeDriver version matches your installed version of Google Chrome. If ChromeDriver is not in your PATH, you'll need to specify its location explicitly in your code.
- All required dependencies are listed in the [`requirements.txt`](requirements.txt) file.
