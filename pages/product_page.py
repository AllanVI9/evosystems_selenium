import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def add_products_to_cart(self, quantity=6):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")[:quantity]

        added_product_names = []

        for product in products:
            name_elem = product.find_element(By.CLASS_NAME, "inventory_item_name")
            product_name = name_elem.text
            added_product_names.append(product_name)
            btn_add = product.find_element(By.XPATH, ".//button[contains(text(),'Add to cart')]")
            btn_add.click()

        return added_product_names

    def remove_products_from_cart(self):
        wait = WebDriverWait(self.driver, 10)
        cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        cart_icon.click()

        while True:
            remove_buttons = self.driver.find_elements(By.XPATH, "//button[contains(text(),'Remove')]")
            if not remove_buttons:
                break
            for btn in remove_buttons:
                try:
                    wait.until(EC.element_to_be_clickable(btn)).click()
                    time.sleep(0.25)
                except Exception as e:
                    print(f"⚠️ Erro ao clicar no botão de remoção: {e}")

        print("✅ Todos os produtos removidos com sucesso.")
