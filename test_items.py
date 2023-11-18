import time

from selenium.common import NoSuchElementException

link = ('http://selenium1py.pythonanywhere.com/catalogue/coders-at'
        '-work_207/')


def test_add_button_exist(browser):
    browser.get(link)
    time.sleep(30)
    try:
        browser.find_element(
            by='class name', value='btn.btn-lg.btn-primary.btn-add-to-basket')
    except NoSuchElementException:
        assert False, 'Button "Add to basket" dont exist'
