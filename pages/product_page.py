from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_product_btn(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET
        ), "Login form is not presented"

    def add_product_to_card(self):
        self.should_be_add_product_btn()
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()

    def get_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        return book_name

    def get_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        return book_price

    def compare_books_name_in_basket_and_in_cataloge(self, book_name):
        book_name_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_BASKET).get_attribute(
            'textContent')
        assert book_name == book_name_in_basket, "Book name in basket is not correct!"

    def compare_price_in_basket_and_in_cataloge(self, book_price):
        baskets_price = self.browser.find_element(*ProductPageLocators.BASKETS_PRICE).text
        book_price_in_msg = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_MSG).text
        assert baskets_price == book_price, "Price in baskets is incorrect"
        assert book_price_in_msg.find(book_price) != -1, "No book price in message!"