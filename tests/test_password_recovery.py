import allure
from pages.password_page import PasswordPage
from urls import Urls
from data import Data

class TestPasswordRecovery:
    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_page_forgot_password(self, driver):
        password_page = PasswordPage(driver)
        password_page.open_url(Urls.LOGIN_PAGE)
        password_page.click_recovery_password_button()
        assert password_page.current_url() == Urls.FORGOT_PASSWORD_URL

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_send_email_and_click_to_recover_password(self, driver):
        password_page = PasswordPage(driver)
        password_page.open_url(Urls.LOGIN_PAGE)
        password_page.click_recovery_password_button()
        password_page.send_email(Data.EMAIL)
        password_page.click_recovery_button()
        assert password_page.current_url() == Urls.RESET_PASSWORD

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_to_show_hide_password(self, driver):
        password_page = PasswordPage(driver)
        password_page.open_url(Urls.LOGIN_PAGE)
        password_page.click_recovery_password_button()
        password_page.send_email(Data.EMAIL)
        password_page.click_recovery_button()
        password_page.click_show_password()
        assert password_page.check_show_password()