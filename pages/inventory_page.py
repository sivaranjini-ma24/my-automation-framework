class InventoryPage:
    def __init__(self, page):
        self.page = page
        # Step 1: Define XPaths for adding items and checking the cart
        self.add_backpack_btn = page.locator("xpath=//button[@id='add-to-cart-sauce-labs-backpack']")
        self.cart_badge = page.locator("xpath=//span[@class='shopping_cart_badge']")

    def add_backpack_to_cart(self):
        # Action to click the add to cart button
        self.add_backpack_btn.click()

    def get_cart_count(self):
        # Action to extract the text number displayed over the cart icon
        return self.cart_badge.text_content()
