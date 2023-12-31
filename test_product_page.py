import pytest

from .pages import links
from .pages.bascet_page import BascetPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .utils import generate_random_string as gen


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = f'{gen.generate_random_string()}@fakemail.com'
        password = gen.generate_random_string()
        link = links.LINK_LOGIN_PAGE
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = links.LINK_PRODUCT_PAGE
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = links.LINK_PRODUCT_PAGE_PROMO
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        page.product_name_match_in_bascet()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = links.LINK_PRODUCT_PAGE_PROMO
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.product_name_match_in_bascet()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = links.LINK_PRODUCT_PAGE
    page = BascetPage(browser, link)
    page.open()
    page.go_to_bascet_page()
    page.bascet_not_empty()
    page.should_be_text_bascet_is_empty()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = links.LINK_PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_success_message_after_adding_product_to_basket(
        browser):
    link = links.LINK_PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = links.LINK_PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.success_message_should_be_dissapear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = links.LINK_PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
