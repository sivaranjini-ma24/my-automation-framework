import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_product_to_cart(page):
    # 1. Initialize the Page Objects
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    
    # 2. Execute the login sequence
    login_page.navigate()
    # SauceDemo provides standard_user as a valid login on their page
    login_page.login("standard_user", "secret_sauce")
    
    # 3. Add item to cart on the landing page
    inventory_page.add_backpack_to_cart()
    
    # 4. Assert that the cart icon now displays "1" item
    assert inventory_page.get_cart_count() == "1"
