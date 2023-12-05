import pytest

from .pages import links
from .pages.bascet_page import BascetPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


@pytest.mark.login_guest
class TestPageFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = links.LINK_MAIN_PAGE
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
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



