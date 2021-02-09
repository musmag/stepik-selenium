from .locators import MainPageLocators
#from .pages.login_page import LoginPage
import time
from .base_page import BasePage

class MainPage(BasePage):

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        time.sleep(3)


    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        time.sleep(3)

#это главная страница, на ней проверяем что ссылка есть