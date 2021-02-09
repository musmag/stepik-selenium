from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", "Сылка несоответсвует"
        print ("Заебись")
        time.sleep(3)
        # реализуйте проверку на корректный url адрес
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма логина отсутсвует"
        print('Ахуенно')
        time.sleep(3)
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.RIG_FORM), 'Форма регистрации отсутсвует'
        print('Суперпупер')
        time.sleep(3)
        # реализуйте проверку, что есть форма регистрации на странице
        assert True