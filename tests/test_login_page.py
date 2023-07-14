from models.login_page import LoginPage
from playwright.sync_api import Page, expect


def test_negative_login(page: Page):
    email = "bogdan@flip.ro"
    password = "test123!"
    login_page = LoginPage(page)
    login_page.login(
        email, password
    )
    expect(login_page.login_message).to_have_text("Această adresă de e-mail nu este asociată cu un cont existent")
