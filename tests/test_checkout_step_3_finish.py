import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
from utils.config import load_all_users

users = [(user["username"], user["password"]) for user in load_all_users()]

@pytest.mark.parametrize("username, password", users)
def test_checkout_step_3_finish(driver, username, password):
    WEBSITE_SUCCESS_MESSAGE = "Thank you for your order!"

    login_page = LoginPage(driver)
    product_page = ProductPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.load()
    login_page.login(username, password)
    product_page.add_products_to_cart(quantity=2)

    checkout_page.start_checkout("nome", "sobrenome", "01234-567")
    checkout_page.finish_checkout()

    print("⏳ Verificando sucesso da compra")
    wait = WebDriverWait(driver, 10)
    success_msg = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header")))
    assert success_msg.text == WEBSITE_SUCCESS_MESSAGE, "❌ Compra não foi finalizada com sucesso"
    print("✅ Compra finalizada com sucesso.")
    time.sleep(0.25)

    login_page.logout_reset()
