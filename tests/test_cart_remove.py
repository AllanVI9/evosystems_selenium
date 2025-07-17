import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from tests.shared import safe_step
from utils.config import load_all_users

users = [(user["username"], user["password"]) for user in load_all_users()]

@pytest.mark.parametrize("username, password", users)
def test_cart_remove(driver, username, password):
    # Carrega o setup do Login
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, password)

    # Carrega o setup do Product
    product_page = ProductPage(driver)

    # Adiciona produtos ao carrinho
    added_product_names = product_page.add_products_to_cart()

    # Remove os produtos do carrinho
    safe_step(lambda: product_page.remove_products_from_cart(), username, "Remover produtos do carrinho")

    # Verifica se os produtos foram removidos da lista do carrinho
    quantity = len(added_product_names)
    products = driver.find_elements(By.CLASS_NAME, "cart_list")[:quantity]
    count = len(products)
    assert 0 == count, f"Esperado 0 itens no carrinho, mas encontrou {count}"

    # Verifica se o número de itens no carrinho está correto
    wait = WebDriverWait(driver, 10)
    cart = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    count = 0
    assert cart.text == str(count), f"Esperado {count} itens no carrinho, mas encontrou {cart.text}"

    login_page.logout_reset()
