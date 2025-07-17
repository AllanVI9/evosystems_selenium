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
def test_cart_add(driver, username, password):
    # Carrega o setup do Login
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, password)

    # Carrega o setup do Product
    product_page = ProductPage(driver)

    # Adiciona produtos ao carrinho
    added_product_names = product_page.add_products_to_cart()
    print(f"🛒 Produtos adicionados ao carrinho: {added_product_names}")

    # Verifica se o número de itens no carrinho está correto
    wait = WebDriverWait(driver, 10)
    cart = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    count = len(added_product_names)
    assert cart.text == str(count), f"Esperado {count} itens no carrinho, mas encontrou {cart.text}"

    # Valida se os itens do carrinho correspondem aos produtos adicionados
    safe_step(lambda: validate_cart_items(driver, added_product_names), username, "Validar itens adicionados ao carrinho")

    # Logout e Reset dos dados
    login_page.logout_reset()

def validate_cart_items(driver, expected_names):
  print("⏳ Aguardando ícone do carrinho clicável")
  wait = WebDriverWait(driver, 15)
  cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
  cart_icon.click()

  print("⏳ Aguardando elementos do carrinho carregarem")
  wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item")))

  cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
  cart_names = [item.text for item in cart_items]

  print(f"🛒 Itens no carrinho: {cart_names}")
  print(f"🛒 Itens esperados: {expected_names}")

  assert cart_names == expected_names, f"Itens no carrinho não batem: esperado {expected_names}, mas encontrou {cart_names}"
  print("✅ Os itens no carrinho correspondem aos produtos adicionados.")
