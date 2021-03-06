from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.get_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()	
		
    def should_be_correct_adding_product_to_basket(self):
        self.add_product_to_basket()
		
        self.should_be_message_about_added_product()
        self.should_be_message_about_current_product()
        self.should_be_message_about_price_basket()
        self.should_be_price_basket_equals_current_product()
		
    def should_be_message_about_added_product(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_PRODUCT_MESSAGE), \
            "Message about added product is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT_MESSAGE), \
           "Message about added product is presented, but should not be"

    def should_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_PRODUCT_MESSAGE), \
           "Message about added product is not disappeared"

    def should_be_message_about_price_basket(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE_MESSAGE), \
            "Message about price of the basket is not presented"

    def should_be_message_about_current_product(self):
        message = self.get_text_of_element(*ProductPageLocators.ADDED_PRODUCT_MESSAGE)
        product_name = self.get_text_of_element(*ProductPageLocators.PRODUCT_NAME)
        assert self.is_equals(message, product_name), \
            "The name of the product in the message doesn't match the product that was added"
		
    def should_be_price_basket_equals_current_product(self):
        bucket_price = self.get_text_of_element(*ProductPageLocators.BASKET_PRICE_MESSAGE)
        product_price = self.get_text_of_element(*ProductPageLocators.PRODUCT_PRICE)
        assert self.is_main_message_contains_sub(bucket_price, product_price), \
            "Basket price doesn't match the product price"