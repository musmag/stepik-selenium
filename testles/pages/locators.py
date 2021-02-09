from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    RIG_FORM = (By.CSS_SELECTOR, '#register_form')

#это локаторы, их выносим для того что бы часто код не переписывать