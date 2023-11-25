from .pages.login_page import LoginPage


def test_login_and_register_form_exist(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
