def test_add_cheapest_product_to_the_cart(home_page):
    """
    Verifies that the cheapest product in the inventory can be added to the cart successfully.
    """
    is_add = home_page.add_cheapest_product_to_the_cart()
    assert "successfully" in is_add
