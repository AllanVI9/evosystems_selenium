import pytest
from utils.driver_factory import create_driver
from utils.config import load_all_users
from pages.login_page import LoginPage
from pages.product_page import ProductPage

@pytest.fixture(scope="session")
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def credentials():
    return load_all_users()

@pytest.fixture
def login_and_add_products(driver):
    user = load_all_users()
    login_page = LoginPage(driver)
    product_page = ProductPage(driver)

    login_page.load()
    login_page.login(user["username"], user["password"])
    added = product_page.add_products_to_cart(quantity=1)

    return driver, added
