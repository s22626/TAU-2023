import unittest
import logging
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        """Explicitly create a Chrome browser instance."""
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)
        logging.info("Chrome browser instance created.")

    def test_page_title(self):
        """Assert that the title of the page says 'Google'."""
        self.browser.get('http://www.google.com')
        logging.info(f"Opened Google homepage. Current page title: {self.browser.title}")
        self.assertIn('Google', self.browser.title)

    def test_search_page_title(self):
        """Assert that Google search returns data for 'Red Hat'."""
        self.browser.get('http://www.google.com')
        logging.info(f"Opened Google homepage. Current page title: {self.browser.title}")

        try:
            button = self.browser.find_element(By.XPATH, "//button[div[text()='Zaakceptuj wszystko']]")
            logging.info("Button found: %s", button)
            button.click()
        except TimeoutException:
            logging.warning("TimeoutException: Button not found")

        # Wait for the cookie overlay to be present and dismiss it
        # Add logs for waiting
        logging.info("Waiting for the cookie overlay to be present.")
        pass

        # Wait for the search input field to be clickable
        element = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.NAME, 'q'))
        )
        logging.info("Search input field is clickable.")
        assert element is not None

        element.send_keys('cute cat' + Keys.RETURN)
        logging.info("Entered 'Red Hat' in the search input field and pressed RETURN.")
        assert self.browser.title.startswith('cute cat')
        logging.info(f"Current page title: {self.browser.title}")

if __name__ == '__main__':
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    unittest.main(verbosity=2)
