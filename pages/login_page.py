class LoginPage:
    def __init__(self, page):
        self.page = page
        # Step 1: Define the XPaths for the Login elements
        self.username_input = page.locator("xpath=//input[@id='user-name']")
        self.password_input = page.locator("xpath=//input[@id='password']")
        self.login_button = page.locator("xpath=//input[@id='login-button']")

    def navigate(self):
        # Action to open the web page
        self.page.goto("https://saucedemo.com")

    def login(self, username, password):
        # Action sequence to complete login
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
