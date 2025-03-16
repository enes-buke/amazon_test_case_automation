import unittest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class BaseTest(unittest.TestCase):
    base_url = 'https://www.amazon.com.tr/'

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.maximize_window()
        self.driver.get('https://www.amazon.com.tr')
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()