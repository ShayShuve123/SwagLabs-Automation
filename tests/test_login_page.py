from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_valid_login(login_page):
    """
    Verifies that a valid username & password successfully navigate to the inventory page.
    """
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    wait = WebDriverWait(login_page.driver, 10)
    wait.until(EC.url_contains("inventory"))
    assert "inventory" in login_page.driver.current_url, "LOGIN failed"


def test_login_with_invalid_password(login_page):
    login_page.enter_username("standard_user")
    login_page.enter_password("wrong_password")
    login_page.click_login()
    error_text = login_page.get_error_text()
    assert "Username and password do not match" in error_text, "Expected invalid login error message"


def test_login_without_password(login_page):
    login_page.enter_username("standard_user")
    login_page.click_login()
    error_text = login_page.get_error_text()
    assert "Password is required" in error_text, "Expected invalid login error message"
