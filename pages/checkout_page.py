from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def start_checkout(self, first_name, last_name, postal_code):
        print("⏳ Indo para o carrinho")
        cart_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_icon.click()
        time.sleep(0.25)

        print("⏳ Clicando em Checkout")
        checkout_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_btn.click()
        time.sleep(0.25)

        print("⏳ Preenchendo formulário de checkout")

        first_name_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        )
        first_name_input.click()
        first_name_input.clear()
        first_name_input.send_keys(first_name)

        last_name_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "last-name"))
        )
        last_name_input.click()
        last_name_input.clear()
        last_name_input.send_keys(last_name)

        postal_code_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "postal-code"))
        )
        postal_code_input.click()
        postal_code_input.clear()
        postal_code_input.send_keys(postal_code)

        time.sleep(0.25)

        print("⏳ Clicando em Continue")
        self.driver.find_element(By.ID, "continue").click()

    def finish_checkout(self):
        print("⏳ Finalizando a compra")
        finish_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "finish")))
        time.sleep(0.25)
        finish_btn.click()
