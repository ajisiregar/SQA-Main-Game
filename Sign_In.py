import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time
import pdb


class TestRegister(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_register_success(self):
        driver = self.driver
        driver.get('https://eklipse.gg/')
        driver.maximize_window()
        self.assertIn('', self.driver.title)
        menu = driver.find_element(By.XPATH, '/html/body/header/div/div/div[3]/a[1]')
        menu.click()
        time.sleep(10)
        driver.find_element(By.ID, 'username').send_keys('ahmadizulkarnain@gmail.com')
        driver.find_element(By.NAME, 'password').send_keys('youtube123')
        log_in = driver.find_element(By.CSS_SELECTOR, '#app > div > div > div > div.section-login.min-vh-100.col-12.col-lg-5 > div > div:nth-child(3) > form > div.form-group.text-center > button')
        log_in.click()
        time.sleep(10)

if __name__ == "__main__":
    unittest.main()