import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.login_page import LoginPage
from utils.config import load_all_users

users = [(user["username"], user["password"]) for user in load_all_users()]

@pytest.mark.parametrize("username, password", users)
def test_login(driver, username, password):
    # Carrega o setup do Login
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, password)

    # Verifica se o Login foi efetuado com sucesso
    try:
        errors = driver.find_elements(By.CLASS_NAME, "error-message-container")
        if errors:
            error_msg = errors[0].text.strip()
            assert False, f"❌ Login falhou para o usuário: {username}: Error: {error_msg}"
        else:
            lista_produtos = driver.find_element(By.ID, "inventory_container")
            assert lista_produtos.is_displayed(), "Lista de produtos não visível após login"
            print(f"✅ Login bem-sucedido com {username}")
            login_page.logout_reset()
    except TimeoutException:
        pytest.fail(f"❌ Erro no login com {username}: Timeout")
    except Exception as e:
        pytest.fail(f"❌ Erro no login com {username}: {e}", pytrace=True)
