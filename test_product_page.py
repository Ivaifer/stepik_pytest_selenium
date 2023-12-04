import pytest
from .pages import links
from .pages.product_page import ProductPage


@pytest.mark.parametrize('link', links.LINKS_PRODUCT_PROMO)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.product_name_match_in_bascet()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = links.LINK_PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = links.LINK_PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
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

def test_guest_can_go_to_login_page_from_product_page (browser):
    link = links.LINK_PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
