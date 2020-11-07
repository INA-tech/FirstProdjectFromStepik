from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_EMAIL = (By.NAME, "login-username")
    LOGIN_PSW = (By.NAME, "login-password")
    LOGIN_BTN = (By.NAME, "login_submit")
    REG_EMAIL = (By.NAME, "registration-email")
    REG_PSW1 = (By.NAME, "registration-password1")
    REG_PSW2 = (By.NAME, "registration-password2")
    REG_BTN = (By.NAME, "registration_submit")
    LOGOUT = (By.ID, "logout_link")


class ProductPageLocators:
    BTN_ADD_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_PRODUCT_PAGE = (By.CSS_SELECTOR, ".product_main > h1")
    PRICE_PRODUCT_PAGE = (By.CSS_SELECTOR, ".product_main .price_color")
    NAME_PRODUCT_BASKET_PAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_PRODUCT_BASKET_PAGE = (By.CSS_SELECTOR, ".fade.in > div > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group > a")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    TEXT_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
    PRODUCT_NOT_FOUND = (By.CSS_SELECTOR, ".hidden-xs > div > h2")
