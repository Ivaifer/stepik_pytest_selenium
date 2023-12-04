from .pages.bascet_page import BascetPage
from .pages.main_page import MainPage
from .pages import links


def test_guest_can_go_to_login_page(browser):
    link = links.LINK_MAIN_PAGE
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = links.LINK_MAIN_PAGE
    page = BascetPage(browser, link)
    page.open()
    page.go_to_bascet_page()
    page.bascet_not_empty()
    page.should_be_text_bascet_is_empty()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = links.LINK_PRODUCT_PAGE
    page = BascetPage(browser, link)
    page.open()
    page.go_to_bascet_page()
    page.bascet_not_empty()
    page.should_be_text_bascet_is_empty()
