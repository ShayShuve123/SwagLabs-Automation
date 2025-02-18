import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage


@pytest.fixture
def login_page():
    """
    Creates and returns a LoginPage instance pointed at 'https://www.saucedemo.com/'.
    After the test ends, closes the browser.
    """
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield LoginPage(driver)
    driver.quit()


@pytest.fixture
def home_page():
    """
    Creates a browser, performs a valid login to reach the Home (inventory) page,
    then returns a HomePage instance.
    After the test ends, closes the browser.
    """
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    wait = WebDriverWait(login_page.driver, 10)
    wait.until(EC.url_contains("inventory"), "Did not reach inventory page after login")
    yield HomePage(driver)
    driver.quit()
