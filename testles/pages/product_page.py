from .locators import ProductPageLocators
from .base_page import BasePage
import time


class ProductPage(BasePage):

    def add_item_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()

        print('Получилось')

    def current_product(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not present"
        assert self.is_element_present(*ProductPageLocators.ALERT_ADDED_TO_CART), "No alert that a product has been added to cart"
        alert_text = self.browser.find_element(*ProductPageLocators.ALERT_ADDED_TO_CART).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name == alert_text, \
            f"The alert contains wrong product name: {alert_text} - {product_name}"
        print('ЗБС книга та же что и в названии')

    def current_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not present"
        assert self.is_element_present(*ProductPageLocators.ALERT_CART_STATUS), "No alert with cart status"
        alert_text = self.browser.find_element(*ProductPageLocators.ALERT_CART_STATUS).text.split()[-1]
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_cost == alert_text, \
            f"Product cost in cart is not equal to the product cost {alert_text} != {product_cost}"
        print('ЗБС и цена та же')


#это часть 4.3.6. тут мы добавили отрицательные проверки
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        self.add_item_to_basket()
        assert self.is_not_element_present(*ProductPageLocators.ALERT_CART_STATUS), "Пидор #1 появился, хотя не должен был"

    def test_guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_CART_STATUS), "Пидор #2 появился, хотя не должен был"

    def test_message_disappeared_after_adding_product_to_basket(self):
        self.add_item_to_basket()
        assert self.is_disappeared(*ProductPageLocators.ALERT_CART_STATUS), "Нет нихуя #3"



