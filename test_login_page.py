from .pages import links
from .pages.login_page import LoginPage


def test_login_and_register_form_exist(browser):
    link = links.LINK_LOGIN_PAGE
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
