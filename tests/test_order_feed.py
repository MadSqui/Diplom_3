import allure
from urls import Urls
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.personal_page import PersonalPage

class TestOrderFeed:
    @allure.title('Eсли кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_order_modal_open(self, driver):
        main_functional = MainPage(driver)
        main_functional.open_url(Urls.BASE_URL)
        main_functional.click_order_feed()
        order_feed = OrderPage(driver)
        order_feed.click_order()
        assert order_feed.order_modal_is_displayed() == True

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_from_history_displayed_order_list(self, driver):
        personal_page = PersonalPage(driver)
        personal_page.open_url(Urls.BASE_URL)
        personal_page.click_personal_account()
        personal_page.send_email_and_password_and_login()
        main_page = MainPage(driver)
        main_page.add_ingredient()
        main_page.click_button_order()
        main_page.check_modal_is_displayed()
        order_number = main_page.get_order_number()
        main_page.click_modal_close()
        main_page.click_order_feed()
        order_page = OrderPage(driver)
        assert order_number in order_page.get_last_order_number()

    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_total_orders_count_increases(self, driver):
        personal_page = PersonalPage(driver)
        personal_page.open_url(Urls.BASE_URL)
        personal_page.click_personal_account()
        personal_page.send_email_and_password_and_login()
        main_page = MainPage(driver)
        main_page.click_order_feed()
        order_page = OrderPage(driver)
        initial_total_orders = order_page.get_count_all_orders()
        main_page.click_construct()
        main_page.add_ingredient()
        main_page.click_button_order()
        main_page.check_modal_is_displayed()
        main_page.click_modal_close()
        main_page.click_order_feed()
        updated_total_orders = order_page.get_count_all_orders()
        assert updated_total_orders > initial_total_orders

    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_today_orders_count_increases(self, driver):
        personal_page = PersonalPage(driver)
        personal_page.open_url(Urls.BASE_URL)
        personal_page.click_personal_account()
        personal_page.send_email_and_password_and_login()
        main_page = MainPage(driver)
        main_page.click_order_feed()
        order_page = OrderPage(driver)
        initial_today_orders = order_page.get_count_today_orders()
        main_page.click_construct()
        main_page.add_ingredient()
        main_page.click_button_order()
        main_page.check_modal_is_displayed()
        main_page.click_modal_close()
        main_page.click_order_feed()
        updated_today_orders = order_page.get_count_today_orders()
        assert updated_today_orders > initial_today_orders

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_order_in_work(self, driver):
        personal_page = PersonalPage(driver)
        personal_page.open_url(Urls.BASE_URL)
        personal_page.click_personal_account()
        personal_page.send_email_and_password_and_login()
        main_page = MainPage(driver)
        main_page.add_ingredient()
        main_page.click_button_order()
        main_page.check_modal_is_displayed()
        order_number = main_page.get_order_number()
        main_page.click_modal_close()
        main_page.click_order_feed()
        order_page = OrderPage(driver)
        assert order_number in order_page.get_order_in_work()