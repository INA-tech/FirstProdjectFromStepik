from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.find('login'), 'URL not correct'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), 'login email not found'
        assert self.is_element_present(*LoginPageLocators.LOGIN_PSW), 'login password not found'
        assert self.is_element_present(*LoginPageLocators.LOGIN_BTN), 'login button not found'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), 'register email not found'
        assert self.is_element_present(*LoginPageLocators.REG_PSW1), 'register password1 not found'
        assert self.is_element_present(*LoginPageLocators.REG_PSW2), 'register password2 not found'
        assert self.is_element_present(*LoginPageLocators.REG_BTN), 'register button not found'

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PSW1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PSW2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BTN).click()
        assert self.is_element_present(*LoginPageLocators.LOGOUT), 'user is not registered'
