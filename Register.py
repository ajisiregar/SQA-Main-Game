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
        menu = driver.find_element(By.XPATH, '/html/body/header/div/div/div[3]/a[2]')
        menu.click()
        time.sleep(10)
        driver.find_element(By.CLASS_NAME, 'form-control').click()
        driver.find_element(By.NAME, 'name').send_keys('Aji')
        driver.find_element(By.NAME, 'email').send_keys('ahmadizulkarnain@gmail.com')
        driver.find_element(By.NAME, 'password').send_keys('youtube123')
        driver.find_element(By.NAME, 'password_confirmation').send_keys('youtube123')
        pdb.set_trace()
        sign_in = driver.find_element(By.CSS_SELECTOR, '#app > div > div > div > div.section-login.min-vh-100.col-12.col-lg-5 > div > div:nth-child(3) > form > div.form-group.text-center.my-4 > button')
        sign_in.click()
        time.sleep(5)

if __name__ == "__main__":
    unittest.main()