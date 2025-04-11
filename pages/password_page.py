import allure
from locators.password_page_locators import PasswordPageLocators
from pages.base_page import BasePage


class PasswordPage(BasePage):
    @allure.step('Клик на кнопку "Восстановить пароль"')
    def click_recovery_password_button(self):
        self.wait_for_load_element(PasswordPageLocators.PASSWORD_RECOVERY_LINK)
        self.find_element(PasswordPageLocators.PASSWORD_RECOVERY_LINK).click()

    @allure.step('Ввести email')
    def send_email(self, email):
        self.wait_for_load_element(PasswordPageLocators.RECOVERY_EMAIL_INPUT)
        self.find_element(PasswordPageLocators.RECOVERY_EMAIL_INPUT).send_keys(email)

    @allure.step('Клик на кнопку "Восстановить"')
    def click_recovery_button(self):
        self.find_element(PasswordPageLocators.RECOVER_BUTTON).click()
        self.wait_for_load_element(PasswordPageLocators.NEW_PASSWORD_INPUT)

    @allure.title('Клик на "Глаз"')
    def click_show_password(self):
        self.find_element(PasswordPageLocators.SHOW_PASSWORD_BUTTON).click()
        self.wait_for_load_element(PasswordPageLocators.HIDE_PASSWORD_BUTTON)

    @allure.step('Проверка, что поле подсвечивается')
    def check_show_password(self):
        if 'input_status_active' in self.find_element(PasswordPageLocators.HIDE_PASSWORD_BUTTON).get_attribute('class'):
            return True
        return False