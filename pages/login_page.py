from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert LoginPageLocators.LOGIN_URL in self.browser.current_url, '"login" not found in url'

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), 'login form not found'

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), 'register form not found'

    def register_new_user(self, email, password):
        register_email = self.browser.find_element(
            *LoginPageLocators.REGISTER_EMAIL)
        register_email.send_keys(email)
        register_password = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD)
        register_password.send_keys(password)
        register_password_repeat = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD_REPEAT)
        register_password_repeat.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
