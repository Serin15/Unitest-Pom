import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from config.config import BASE_URL, USERNAME, PASSWORD
from pages.login_page import LoginPage


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)

    def setUp(self):
        self.page = LoginPage(self.driver)
        self.page.load_page(BASE_URL)

    def test_valid_login(self):
        self.page.login(USERNAME, PASSWORD)
        self.assertIn("successfully", self.driver.current_url)

    def test_invalid_login(self):
        self.page.login("wrong_user", "wrong_password")
        error_message = self.driver.find_element(By.ID, "error").text
        self.assertIn("Your username is invalid!", error_message)

    def tearDown(self):
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()