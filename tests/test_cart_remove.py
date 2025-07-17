import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from tests.shared import safe_step
from utils.config import load_all_users

# Carrega todos os usuários da lista de credenciais
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
    print(f"🛒 Produtos adicionados ao carrinho: {added_product_names}")

    # Remove os produtos do carrinho
    safe_step(lambda: product_page.remove_products_from_cart(), username, "Remover produtos do carrinho")

    # Verifica se os produtos foram removidos da lista do carrinho
    quantity = len(added_product_names)
    products = driver.find_elements(By.CLASS_NAME, "cart_list")[:quantity]
    count = len(products)

    # É esperado 1 item, pois existe um item de título padrão não removível na lista do carrinho
    assert 1 == count, f"Esperado 1 itens no carrinho, mas encontrou {count}"

    # Verifica se o contador visível do número de itens do carrinho foi removido
    wait = WebDriverWait(driver, 5)
    cart_badge_is_removed = wait.until(EC.invisibility_of_element_located((By.ID, "shopping_cart_badge")))
    assert cart_badge_is_removed, "Esperado que o contador visível do carrinho não esteja mais visível após a remoção de todos os produtos"

    # Logout e Reset dos dados
    login_page.logout_reset()
