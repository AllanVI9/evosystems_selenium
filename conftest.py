import pytest
from utils.driver_factory import create_driver
from utils.config import load_all_users

@pytest.fixture(scope="session")
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def credentials():
    return load_all_users()
