import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.shared import reset

class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def login(self, username: str, password: str):
        reset(self.driver)
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def logout_reset(self):
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1.5)
        self.driver.find_element(By.ID, "logout_sidebar_link").click()
        reset(self.driver)
