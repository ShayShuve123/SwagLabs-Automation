from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    This class represents the Login page of the Swag Labs application.
    It provides methods to enter username, password, and perform the login action.
    """

    def __init__(self, driver):
        """
        Initializes the LoginPage instance.

        :param driver: WebDriver instance pointing to the login page ('https://www.saucedemo.com/').
        """
        self.driver = driver

    def get_username_box(self):
        """
        Waits for the username box to become visible.

        :return: WebElement for the username input field.
        :raises TimeoutException: If element not found within 10 seconds.
        """
        wait = WebDriverWait(self.driver, 10)
        return wait.until(
            EC.visibility_of_element_located((By.ID, "user-name")),
            "Username box not found"
        )

    def get_password_box(self):
        """
        Waits for the password box to become visible.
        return: WebElement for the password input field.
        """
        wait = WebDriverWait(self.driver, 10)
        return wait.until(
            EC.visibility_of_element_located((By.ID, "password")), "Password box not found"
        )

    def get_login_button(self):
        """ Waits for the login button to become clickable.
           return: WebElement for the login button.
        """
        wait = WebDriverWait(self.driver, 10)
        return wait.until(
            EC.element_to_be_clickable((By.ID, "login-button")), "Login button not clickable"
        )

    def get_error_text(self):
        """
        Retrieves the error message (if any) that appears after a failed login attempt.

        :return: The error text as a string if visible, otherwise an empty string.
        """
        try:
            wait = WebDriverWait(self.driver, 3)
            elem = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']"))
            )
            return elem.text
        except TimeoutException:
            return ""

    def enter_username(self, username):
        """Enters the given username in the username input field"""
        username_box = self.get_username_box()
        username_box.clear()
        username_box.send_keys(username)

    def enter_password(self, password):
        """Enters the given password in the password input field"""
        password_box = self.get_password_box()
        password_box.clear()
        password_box.send_keys(password)

    def click_login(self):
        """
        Clicks the login button.
        """
        btn = self.get_login_button()
        btn.click()
