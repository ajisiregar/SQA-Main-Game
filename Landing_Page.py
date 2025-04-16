import unittest # Framework testing Python
from selenium import webdriver # Webdriver to control browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time # for manual delay
import pdb # for manual debugging


class TestLandingPage(unittest.TestCase): #class contain all of the test case
    def setUp(self): # default function of unittest
        self.driver = webdriver.Chrome() # method to start at chrome

    def test_001_landing_page_sign_in(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        driver.get('https://eklipse.gg/')
        driver.maximize_window()
        sign_in = driver.find_element(By.XPATH, '/html/body/header/div/div/div[3]/a[1]')
        sign_in.click()
        wait

    def test_002_landing_page_sign_up(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        driver.get('https://eklipse.gg/')
        driver.maximize_window()
        sign_up = driver.find_element(By.XPATH, '/html/body/header/div/div/div[3]/a[2]')
        sign_up.click()
        wait
if __name__ == "__main__":
    unittest.main() # default running test from unittest