from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_basket_empty(self):
        assert self.browser.find_element(*BasketPageLocators.TEXT_ABOUT_EMPTY_BASKET), \
            "Product text about empty basket not found"

    def should_be_not_found_product(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_NOT_FOUND), \
            "Product in backet not found"
