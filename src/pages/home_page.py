from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class HomePage:
    """
    This class represents the Home (Inventory) page of the Swag Labs application.
    It provides methods to list inventory items, find the cheapest product, and add it to cart.
    """

    def __init__(self, driver):
        self.driver = driver

    # get the inventory_list lop and by the product with the lower price
    def get_inventory_list(self):
        """
        Waits for the inventory container to appear, then returns a list of WebElements
        representing each inventory item.

        :return: A list of WebElements (each having class 'inventory_item').
        :raises TimeoutException: If the container is not found within the given time.
        """
        try:
            wait = WebDriverWait(self.driver, 10)
            container = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")),
                "Expected 'inventory_list' container not found"
            )
            items = container.find_elements(By.CLASS_NAME, "inventory_item")
            return items
        except TimeoutException:
            return []

    def find_the_cheapest_product(self):
        """
        Finds the inventory item with the lowest price by parsing each item's price element.
        If multiple items have the same lowest price, returns the first occurrence.

        :return: The WebElement corresponding to the cheapest product.
                 If no products are found, returns None.
        """
        inventory_list = self.get_inventory_list()
        if not inventory_list:
            print("No inventory items found.")
            return None

        cheapest_item = None
        min_price = float('inf')

        for item in inventory_list:
            price_element = item.find_element(By.CLASS_NAME, "inventory_item_price")
            product_price = float(price_element.text.replace("$", ""))

            if product_price < min_price:
                min_price = product_price
                cheapest_item = item

        return cheapest_item

    def add_cheapest_product_to_the_cart(self):
        """
        Finds and adds the cheapest product to the cart by clicking its button.
        Then verifies if the button text changes to 'Remove'.

        :return: A message indicating success if the product was added,
                 or a message indicating a failure scenario.
        """
        cheapest_product = self.find_the_cheapest_product()
        if cheapest_product is None:
            return "No items to add. Possibly the inventory is empty."

        # Look for the 'Add to cart'/'Remove' button
        btn = cheapest_product.find_element(By.CLASS_NAME, "btn_inventory")
        btn.click()

        # After the click, the DOM might refresh, so find the button again
        btn = cheapest_product.find_element(By.CLASS_NAME, "btn_inventory")
        if btn.text.lower() == "remove":
            return "Product added successfully to the cart 🛒"
        return "Failed to add product to cart"
