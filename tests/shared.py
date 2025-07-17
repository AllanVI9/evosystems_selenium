import pytest

def safe_step(step_func, username, label):
  try:
      step_func()
  except AssertionError as e:
      pytest.fail(f"❌ Erro ao {label} para {username}: {e}", pytrace=True)
  except Exception as e:
      pytest.fail(f"❌ Erro inesperado ao {label} para {username}: {e}", pytrace=True)

def reset(driver):
    driver.delete_all_cookies()
    driver.execute_script("window.localStorage.clear();")
    driver.execute_script("window.sessionStorage.clear();")
    driver.refresh()
