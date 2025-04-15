import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import pdb


class TestLandingPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_landing_page(self):
        driver = self.driver
        driver.get('https://eklipse.gg/')
        driver.maximize_window()
        self.assertIn('', self.driver.title)
        menu = driver.find_element(By.XPATH, '/html/body/main/div/div[6]/div[2]/div[1]/div[1]/div')

if __name__ == "__main__":
    unittest.main()