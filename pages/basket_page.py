from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), \
            "The message that basket is empty is not presented on basket page"
	
    def is_not_basket_contains_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TITLE), \
            "There are products in the basket, but it shouldn't be"