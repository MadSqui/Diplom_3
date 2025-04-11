import allure
from pages.base_page import BasePage
from locators.personal_page_locators import PersonalPageLocators
from locators.main_page_locators import MainPageLocators
from data import Data

class PersonalPage(BasePage):
    @allure.step('Клик на кнопку "Личный кабинет"')
    def click_personal_account(self):
        self.wait_for_load_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.find_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    @allure.step('Ввести email')
    def send_email(self):
        self.find_element(MainPageLocators.EMAIL_INPUT).send_keys(Data.EMAIL)

    @allure.step('Ввести пароль')
    def send_password(self):
        self.find_element(MainPageLocators.PASSWORD_INPUT).send_keys(Data.PASSWORD)

    @allure.step('Клик на кнопку "Войти"')
    def click_button_login(self):
        self.wait_for_load_element(PersonalPageLocators.LOGIN_BUTTON)
        self.find_element(PersonalPageLocators.LOGIN_BUTTON).click()

    @allure.step('Авторизация')
    def send_email_and_password_and_login(self):
        self.send_email()
        self.send_password()
        self.click_button_login()
        self.wait_for_load_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Клик на кнопку "История заказов"')
    def click_history_order(self):
        self.wait_for_load_element(PersonalPageLocators.ORDER_HISTORY_LINK)
        self.find_element(PersonalPageLocators.ORDER_HISTORY_LINK).click()

    @allure.step('Клик на кнопку "Выход"')
    def click_logout(self):
        self.wait_for_load_element(PersonalPageLocators.LOGOUT_BUTTON)
        self.find_element(PersonalPageLocators.LOGOUT_BUTTON).click()
        self.wait_for_load_element(MainPageLocators.EMAIL_INPUT)