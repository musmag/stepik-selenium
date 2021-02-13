from .pages.product_page import ProductPage
import time
import pytest
from .pages.base_page import BasePage




#тут с параметризацей ссылок все понятно, ставим ссылку, в нее передаем параметр
#что бы заюзать пометку непроходящего заведомо теста, надо использовать marks
@pytest.mark.tentests
class TestTen():
    @pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
    def test_guest_can_add_product_to_basket(self, browser, link):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}'
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()
        page.add_item_to_basket()
        page.solve_quiz_and_get_code()
        time.sleep(3)
        page.current_product()
        page.current_price()
    #time.sleep(5)


#под параметром нигга идут заведомо упавшие проверки из задания 4.3.6.
@pytest.mark.nigga
class TestNigga():
    @pytest.mark.xfail
    def test_waits_add_and_check(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()
        page.test_guest_cant_see_success_message_after_adding_product_to_basket()


    def test_waits_check(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()
        page.test_guest_cant_see_success_message()


    @pytest.mark.xfail
    def test_waits_dissapeared(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()
        page.test_message_disappeared_after_adding_product_to_basket()

@pytest.mark.see
class TestSee():
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()


    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = BasePage(browser, browser.current_url)
        login_page.go_to_login_page()