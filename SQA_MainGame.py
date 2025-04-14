import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class TestMenuHover(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_menu_hover(self):
        driver = self.driver
        driver.get('https://eklipse.gg/')
        driver.maximize_window()
        self.assertIn('', self.driver.title)
        menu = driver.find_element(By.XPATH, '/html/body/header/div/div/div[2]/nav/ul/li[1]/a')
        actions = ActionChains(driver)
        actions.move_to_element(menu).perform()
        time.sleep(2)
        submenu = driver.find_element(By.XPATH,'/html/body/header/div/div/div[2]/nav/ul/li[1]/ul/li/div/div/div[1]/div[2]/div/div[6]/a')
        submenu.click()
        time.sleep(5)
    def test_sign_in(self):
        driver = self.driver
        driver.get('https://eklipse.gg/')
        driver.maximize_window()
        self.assertIn('', self.driver.title)
        menu = driver.find_element(By.XPATH, '/html/body/header/div/div/div[3]/a[1]')
        menu.click()
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()