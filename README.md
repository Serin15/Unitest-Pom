
# Selenium POM Test Project

This is an automated testing project using **Selenium WebDriver**, organized according to the **Page Object Model (POM)** and utilizing **unittest** for running tests.

## Project Structure

```
Selenium_pom1/
│── config/            # Project configuration
│   ├── config.py
│── pages/             # Page object files
│   ├── login_page.py
│── reports/           # Generated test reports
│── tests/             # Unit tests
│   ├── test_login.py
│── requirements.txt   # Project dependencies
│── run_tests.py       # Main test execution script
```

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/user/Selenium_pom1.git
   cd Selenium_pom1
   ```

2. **Create and activate a virtual environment**:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # For Mac/Linux
   .venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

## Running Tests

To execute tests, use the following command:
```sh
python run_tests.py
```

### Generating an HTML Report

After running the tests, an HTML report will be generated in the **reports/** directory.

## Contribution

1. **Fork** this repository.
2. Create a **new branch** (`new-feature`):
   ```sh
   git checkout -b new-feature
   ```
3. Make the necessary changes and **commit** them:
   ```sh
   git commit -m "Added new feature"
   ```
4. **Push the changes to GitHub**:
   ```sh
   git push origin new-feature
   ```
5. Open a **Pull Request**.

## License

This project is distributed under the MIT License.

---
### Contact
If you have any questions or suggestions, feel free to reach out!

