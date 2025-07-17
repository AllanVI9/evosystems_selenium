import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
from utils.config import load_all_users

# Carrega todos os usuários da lista de credenciais
users = [(user["username"], user["password"]) for user in load_all_users()]

@pytest.mark.parametrize("username, password", users)
def test_checkout_step_1_fill_fields(driver, username, password):
    FIRST_NAME_MESSAGE = "Error: First Name is required"
    LAST_NAME_MESSAGE = "Error: Last Name is required"
    POSTAL_CODE_MESSAGE = "Error: Postal Code is required"

    # Carrega o setup do Login
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, password)

    # Carrega o setup do Product
    product_page = ProductPage(driver)

    # Adiciona produtos ao carrinho
    added_product_names = product_page.add_products_to_cart(quantity=2)
    print(f"🛒 Produtos adicionados ao carrinho: {added_product_names}")

    # Carrega o setup do Checkout
    checkout_page = CheckoutPage(driver)

    # Verifica se ao clicar no botão 'Continue' as mensagens de erro referente aos campos não preenchidos são exibidas
    fields_pack = [1,2,3,4]
    for field_pack in fields_pack:
        print("Testando campo :", field_pack)
        if field_pack == 1:
            checkout_page.start_checkout("", "", "")
        elif field_pack == 2:
            checkout_page.start_checkout("nome", "", "")
        elif field_pack == 3:
            checkout_page.start_checkout("nome", "sobrenome", "")
        elif field_pack == 4:
            checkout_page.start_checkout("nome", "sobrenome", "01234-567")
        try:
            errors = driver.find_elements(By.CLASS_NAME, "error-message-container")
            if errors:
                error_msg = errors[0].text.strip()
                if field_pack == 1:
                    assert error_msg == FIRST_NAME_MESSAGE, f"'{error_msg}'"
                elif field_pack == 2:
                    assert error_msg == LAST_NAME_MESSAGE, f"'{error_msg}'"
                elif field_pack == 3:
                    assert error_msg == POSTAL_CODE_MESSAGE, f"'{error_msg}'"
                elif field_pack == 4:
                    assert not error_msg.is_displayed(), f"'{error_msg}'"
        except TimeoutException:
             pytest.fail(f"❌ Checkout falhou para o usuário: {username}: Timeout")
        except Exception as e:
             pytest.fail(f"❌ Checkout falhou para o usuário: {username}: {e}", pytrace=True)

    print(f"✅ Todos os campos preenchidos com sucesso!")

    # Logout e Reset dos dados
    login_page.logout_reset()
