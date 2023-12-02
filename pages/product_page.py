from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        self.browser.find_element(
            *ProductPageLocators.BUTTON_ADD_TO_BASKET).click()

    def product_name_match_in_bascet(self):
        name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_PAGE).text
        message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_BASCET).text
        assert name == message, 'Product name not matching'

    def product_price_match_in_bascet(self):
        price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_IN_PAGE).text
        message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_IN_BASCET).text
        assert price ==  message, 'Product price not matching'
