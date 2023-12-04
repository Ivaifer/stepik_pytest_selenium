from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')


class BascetPageLocators:
    BASCET_LINK = (By.CSS_SELECTOR, 'span.btn-group>a')
    BASCET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner>p')
    BASCET_NOT_EMPTY = (By.CLASS_NAME, 'basket-items')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_URL = 'login'


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME_IN_BASCET = (
        By.CSS_SELECTOR, '#messages>div:nth-child(1)>div>strong')
    PRODUCT_PRICE_IN_BASCET = (By.CSS_SELECTOR,
                               '#messages>div.alert.alert-safe.alert-noicon.alert-info.fade.in>div>p:nth-child(1)>strong')
    PRODUCT_NAME_IN_PAGE = (By.CSS_SELECTOR, 'div.product_main h1')
    PRODUCT_PRICE_IN_PAGE = (By.CSS_SELECTOR, 'p.price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages>div:nth-child(1)>div')
