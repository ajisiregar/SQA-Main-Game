import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time
import pdb


class TestHome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_Home(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        driver.get('https://eklipse.gg/')
        driver.maximize_window()
        self.assertIn('', self.driver.title)
        menu = driver.find_element(By.XPATH, '/html/body/header/div/div/div[3]/a[1]')
        menu.click()
        wait
        driver.find_element(By.ID, 'username').send_keys('ahmadizulkarnain@ymail.com')
        driver.find_element(By.NAME, 'password').send_keys('youtube123')
        log_in = driver.find_element(By.CSS_SELECTOR, '#app > div > div > div > div.section-login.min-vh-100.col-12.col-lg-5 > div > div:nth-child(3) > form > div.form-group.text-center > button')
        log_in.click()
        wait
        pdb.set_trace()

if __name__ == "__main__":
    unittest.main()