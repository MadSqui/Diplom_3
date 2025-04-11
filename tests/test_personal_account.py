import allure
from urls import Urls
from pages.personal_page import PersonalPage

class TestPersonalAccount:
    @allure.title('Переход по клику на «Личный кабинет»')
    def test_go_to_personal_account(self,driver):
        personal_account = PersonalPage(driver)
        personal_account.open_url(Urls.BASE_URL)
        personal_account.click_personal_account()
        assert personal_account.current_url() == Urls.LOGIN_PAGE

    @allure.title('Переход в раздел «История заказов»')
    def test_go_to_order_history(self,driver):
        personal_account = PersonalPage(driver)
        personal_account.open_url(Urls.BASE_URL)
        personal_account.click_personal_account()
        personal_account.send_email_and_password_and_login()
        personal_account.click_personal_account()
        personal_account.click_history_order()
        assert personal_account.current_url() == Urls.ORDER_HISTORY

    @allure.title('Выход из аккаунта')
    def test_logout(self,driver):
        personal_account = PersonalPage(driver)
        personal_account.open_url(Urls.ORDER_HISTORY)
        personal_account.click_personal_account()
        personal_account.send_email_and_password_and_login()
        personal_account.click_personal_account()
        personal_account.click_logout()
        assert personal_account.current_url() == Urls.ORDER_HISTORY