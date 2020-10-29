from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL = (By.NAME, "login-username")
    LOGIN_PSW = (By.NAME, "login-password")
    LOGIN_BTN = (By.NAME, "login_submit")

    REG_EMAIL = (By.NAME, "registration-email")
    REG_PSW1 = (By.NAME, "registration-password1")
    REG_PSW2 = (By.NAME, "registration-password2")
    REG_BTN = (By.NAME, "registration_submit")
