import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
from utils.config import load_all_users

users = [(user["username"], user["password"]) for user in load_all_users()]

@pytest.mark.parametrize("username, password", users)
def test_checkout_step_2_next(driver, username, password):
    login_page = LoginPage(driver)
    product_page = ProductPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.load()
    login_page.login(username, password)
    added_products = product_page.add_products_to_cart(quantity=2)

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
                first_name = driver.find_element(By.ID, "first-name").get_attribute("value")
                last_name = driver.find_element(By.ID, "last-name").get_attribute("value")
                postal_code = driver.find_element(By.ID, "postal-code").get_attribute("value")
                error_msg = errors[0].text.strip()
                if field_pack == 1:
                    assert first_name == "", f"❌ Campo 'Fist Name' inválido!"
                    assert last_name == "", f"❌ Campo 'Last Name' inválido!"
                    assert postal_code == "", f"❌ Campo 'Postal Code' inválido!"
                    assert not "checkout-step-two.html" in driver.current_url, f"❌ Não deveria ter avançado para o próximo passo do checkout: {error_msg}"
                elif field_pack == 2:
                    assert first_name != "", f"❌ Campo 'Fist Name' inválido!"
                    assert last_name == "", f"❌ Campo 'Last Name' inválido!"
                    assert postal_code == "", f"❌ Campo 'Postal Code' inválido!"
                    assert not "checkout-step-two.html" in driver.current_url, f"❌ Não deveria ter avançado para o próximo passo do checkout: {error_msg}"
                elif field_pack == 3:
                    assert first_name != "", f"❌ Campo 'Fist Name' inválido!"
                    assert last_name != "", f"❌ Campo 'Last Name' inválido!"
                    assert postal_code == "", f"❌ Campo 'Postal Code' inválido!"
                    assert not "checkout-step-two.html" in driver.current_url, f"❌ Não deveria ter avançado para o próximo passo do checkout: {error_msg}"
                elif field_pack == 4:
                    assert first_name != "", f"❌ Campo 'Fist Name' inválido!"
                    assert last_name != "", f"❌ Campo 'Last Name' inválido!"
                    assert postal_code != "", f"❌ Campo 'Postal Code' inválido!"
        except TimeoutException:
             pytest.fail(f"❌ Checkout falhou para o usuário: {username}: Timeout")
        except Exception as e:
             pytest.fail(f"❌ Checkout falhou para o usuário: {username}: {e}", pytrace=True)

    assert "checkout-step-two.html" in driver.current_url, f"❌ Não avançou para o segundo passo do checkout: {error_msg}"
    print(f"✅ Checkout iniciado com sucesso com {len(added_products)} produto(s): {added_products}")

    login_page.logout_reset()
