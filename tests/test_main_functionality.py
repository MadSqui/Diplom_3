import allure
from pages.main_page import MainPage
from pages.personal_page import PersonalPage
from urls import Urls


class TestMainFunctionality:
    @allure.title('Переход по клику в «Конструктор»')
    def test_go_to_construct(self, driver):
        main_functional = MainPage(driver)
        main_functional.open_url(Urls.LOGIN_PAGE)
        main_functional.click_construct()
        assert main_functional.current_url() == Urls.BASE_URL

    @allure.title('Переход по клику в «Ленту заказов»')
    def test_go_to_order_feed(self, driver):
        main_functional = MainPage(driver)
        main_functional.open_url(Urls.LOGIN_PAGE)
        main_functional.click_order_feed()
        assert main_functional.current_url() == Urls.FEED_PAGE

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient(self, driver):
        main_functional = MainPage(driver)
        main_functional.open_url(Urls.BASE_URL)
        main_functional.click_ingredient()
        assert main_functional.get_text_window_ingredient() == 'Детали ингредиента'

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_click_ingredient_and_close_window(self, driver):
        main_functional = MainPage(driver)
        main_functional.open_url(Urls.BASE_URL)
        main_functional.click_ingredient()
        main_functional.close_ingredient_window()
        assert main_functional.get_text_collect_burger() == 'Соберите бургер'

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_add_ingredient_count(self, driver):
        main_functional = MainPage(driver)
        main_functional.open_url(Urls.BASE_URL)
        main_functional.add_ingredient()
        assert main_functional.get_count_bun() == '2'

    @allure.title('Авторизованный пользователь может оформить заказ')
    def test_create_order_with_login_user(self, driver):
        personal_page = PersonalPage(driver)
        personal_page.open_url(Urls.LOGIN_PAGE)
        personal_page.send_email_and_password_and_login()
        main_functional = MainPage(driver)
        main_functional.add_ingredient()
        main_functional.click_button_order()
        assert main_functional.check_modal_is_displayed() == True