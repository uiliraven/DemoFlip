from playwright.sync_api import Page
# Import the necessary module to access the Page class from the Playwright sync API


class LoginPage:
    def __init__(self, page: Page):
        # Constructor method for the LoginPage class, taking a Page object as an argument
        self.page = page
        # Assign the passed Page object to an instance variable called "page"
        self.page.goto("https://flip.ro/autentifica-te/")
        # Accept cookie window
        self.page.get_by_role("button", name="Da, sunt de acord").click()
        # Navigate the page to the specified URL
        self.email_input = self.page.get_by_role("textbox", name="E-mail")
        # Find an element by its placeholder attribute value and assign it to the "email_input" instance variable
        self.password_input = self.page.get_by_role("textbox", name="Parola")
        # Find an element by its placeholder attribute value and assign it to the "password_input" instance variable
        self.btn_login = self.page.get_by_role("button", name="Acceseaza cont")
        # Find a button element with the specified role and name attributes
        # and assign it to the "btn_login" instance variable
        self.login_message = self.page.get_by_text("Această adresă de e-mail nu este asociată cu un cont existent")
        # Locate an element using a CSS selector and assign it to the "login_message" instance variable

    def login(self, email, password):
        # Method for performing the login action, taking the username and password as arguments
        self.email_input.fill(email)
        # Fill in the email input field with the provided username
        self.password_input.fill(password)
        # Fill in the password input field with the provided password
        self.btn_login.click()
        # Click on the login button to submit the form
