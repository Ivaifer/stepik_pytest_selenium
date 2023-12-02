from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_URL = 'login'


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME_IN_BASCET = (By.CSS_SELECTOR, '#messages>div:nth-child(1)>div>strong')
    PRODUCT_PRICE_IN_BASCET = (By.CSS_SELECTOR, '#messages>div.alert.alert-safe.alert-noicon.alert-info.fade.in>div>p:nth-child(1)>strong')
    PRODUCT_NAME_IN_PAGE = (By.CSS_SELECTOR, 'div.product_main h1')
    PRODUCT_PRICE_IN_PAGE = (By.CSS_SELECTOR, 'p.price_color')