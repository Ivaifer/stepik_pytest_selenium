import pytest

LINK_MAIN_PAGE = 'http://selenium1py.pythonanywhere.com'
LINK_CATALOGUE_PAGE = 'http://selenium1py.pythonanywhere.com/catalogue'
LINK_PRODUCT_PAGE = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'
LINK_PRODUCT_PROMO = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
LINKS_PRODUCT_PROMO = [
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6',
    pytest.param(
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7',
        marks=pytest.mark.xfail),
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9']
LINK_LOGIN_PAGE = 'http://selenium1py.pythonanywhere.com/accounts/login'
LINK_BASCET_CASE = 'http://selenium1py.pythonanywhere.com/ru/basket'
