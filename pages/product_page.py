from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_basket_link(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_BASKET), "Button add to basket is not presented"

    def name_on_product_page(self):
        assert self.is_element_present(
            *ProductPageLocators.NAME_PRODUCT_PAGE), "Name product on product page is not presented"
        return self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_PAGE).text

    def price_on_product_page(self):
        assert self.is_element_present(
            *ProductPageLocators.PRICE_PRODUCT_PAGE), "Price product on product page is not presented"
        return self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_PAGE).text

    def should_add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BTN_ADD_BASKET).click()

    def should_be_press_btn_add_to_basket(self):
        self.should_add_to_basket()
        self.solve_quiz_and_get_code()
        assert self.name_on_product_page() == self.browser.find_element(
            *ProductPageLocators.NAME_PRODUCT_BASKET_PAGE).text, "Name product on basket page is wrong"
        assert self.price_on_product_page() == self.browser.find_element(
            *ProductPageLocators.PRICE_PRODUCT_BASKET_PAGE).text, "Price product on basket page is wrong"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Negative test. Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Negative test. Success message not disappeared"
