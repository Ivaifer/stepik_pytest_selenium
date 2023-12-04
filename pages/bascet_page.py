from .base_page import BasePage
from .locators import BascetPageLocators, ProductPageLocators


class BascetPage(BasePage):
    def should_be_text_bascet_is_empty(self):
        assert self.is_element_present(
            *BascetPageLocators.BASCET_IS_EMPTY_MESSAGE),\
            'Empty text is not present, but should be'

    def bascet_not_empty(self):
        assert self.is_not_element_present(
            *BascetPageLocators.BASCET_NOT_EMPTY),\
            'You bascet is not empty, but should be'

    def add_to_cart(self):
        self.browser.find_element(
            *ProductPageLocators.BUTTON_ADD_TO_BASKET).click()
