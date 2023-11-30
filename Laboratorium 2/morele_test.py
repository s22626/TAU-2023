import time
import unittest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By

class MoreleNetTestCase(unittest.TestCase):

    def setUp(self):
        """Explicitly create a Chrome browser instance."""
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)
        logging.info("Chrome browser instance created.")

    def test_login_with_wrong_email(self):
        """Test login with incorrect email on Morele.net."""

        # Open Morele.net website
        self.browser.get('https://www.morele.net/')
        logging.info(f"Opened Morele.net homepage. Current page title: {self.browser.title}")

        # Click the login button
        login_button = self.browser.find_element(By.XPATH, "//span[contains(text(), 'Zaloguj się')]")
        login_button.click()
        logging.info("Clicked on the 'Zaloguj się' button.")

        # Enter wrong email
        email_input = self.browser.find_element(By.ID, 'username')
        email_input.clear()  # Clear any existing value
        email_input.send_keys('good')
        logging.info("Entered incorrect email.")

        time.sleep(5)
        # Find the error message
        error_message = self.browser.find_element(By.CLASS_NAME, 'form-control-error')
        expected_error_message = 'Podaj poprawny adres e-mail!'
        self.assertEqual(error_message.text, expected_error_message,
                         f"Expected: {expected_error_message}, Actual: {error_message.text}")


if __name__ == '__main__':
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    unittest.main(verbosity=2)
