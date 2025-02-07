🖥️ Selenium POM - Automated Testing with Python

This project is an automated testing framework based on Python, Selenium, unittest, and HTMLTestRunner. It uses the Page Object Model (POM) for better code organization.

📌 Features

Automated tests for login functionality

Uses the Page Object Model (POM)

Automatically generates HTML reports

Supports multiple test cases

🛠️ Technologies Used

Python 3.x

Selenium - for browser automation

unittest - testing framework

HTMLTestRunner - generates HTML test reports

🚀 Installation and Setup

Clone the repository:

git clone https://github.com/user/Selenium_POM.git
cd Selenium_POM

Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows

Install dependencies:

pip install -r requirements.txt

🏃‍♂️ Running Tests

To execute the tests, run the following command:

python run_tests.py

📊 Viewing the HTML Report

After running the tests, an HTML report is automatically generated in the reports/ directory.
To view the report, open the Report name_YYYY-MM-DD_HH-MM-SS.html file in a browser.

🏗️ Project Structure

Selenium_POM/
│── config/             # General configurations
│── pages/              # Page Object Model (POM)
│── tests/              # Automated tests
│── reports/            # Generated HTML reports
│── requirements.txt    # Dependencies
│── run_tests.py        # Test runner
│── README.md           # Project documentation

🤝 Contribution

If you want to contribute to this project:

Fork the repository

Create a new branch: git checkout -b feature/new-feature

Make the necessary changes and commit: git commit -m 'Added new feature'

Submit a Pull Request

📜 License

This project is licensed under the MIT License. You are free to use, modify, and distribute this code.

🔥 Happy Testing! 🚀
