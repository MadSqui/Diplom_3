import time
import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    @allure.step('Клик на кнопку "Конструктор"')
    def click_construct(self):
        self.wait_for_load_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.find_element(MainPageLocators.CONSTRUCTOR_BUTTON).click()
        self.wait_for_load_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Клик на кнопку "Лента Заказов"')
    def click_order_feed(self):
        time.sleep(3)
        self.wait_for_clickable_element(MainPageLocators.ORDER_FEED_BUTTON)
        self.find_element(MainPageLocators.ORDER_FEED_BUTTON).click()
        self.wait_for_load_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Клик на ингредиент')
    def click_ingredient(self):
        self.wait_for_load_element(MainPageLocators.INGREDIENT_IMAGE)
        self.find_element(MainPageLocators.INGREDIENT_IMAGE).click()
        self.wait_for_load_element(MainPageLocators.INGREDIENT_DETAILS_MODAL_TITLE)

    @allure.step('Получаем текст окна с ингредиентами')
    def get_text_window_ingredient(self):
        return self.get_text_for_element(MainPageLocators.INGREDIENT_DETAILS_MODAL_TITLE)

    @allure.step('Клик на крестик')
    def close_ingredient_window(self):
        self.find_element(MainPageLocators.MODAL_CLOSE_BUTTON).click()

    @allure.step('Получаем текст "Соберите бургер"')
    def get_text_collect_burger(self):
        return self.get_text_for_element(MainPageLocators.BURGER_CONSTRUCTOR_TITLE)

    @allure.step('Добавляем ингредиент в заказ')
    def add_ingredient(self):
        self.wait_for_load_element(MainPageLocators.INGREDIENT_IMAGE)
        self.drag_and_drop(MainPageLocators.INGREDIENT_IMAGE, MainPageLocators.BASKET_SECTION)

    @allure.step('Получаем количество булок')
    def get_count_bun(self):
        time.sleep(2)
        return self.get_text_for_element(MainPageLocators.BUN_COUNTER)

    @allure.step('Клик на кнопку "Оформить заказ"')
    def click_button_order(self):
        self.wait_for_load_element(MainPageLocators.PLACE_ORDER_BUTTON)
        self.find_element(MainPageLocators.PLACE_ORDER_BUTTON).click()

    @allure.step('Проверка отображения модального окна с номером заказа')
    def check_modal_is_displayed(self):
        self.wait_for_clickable_element(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_for_load_element(MainPageLocators.ORDER_ID_TITLE)
        return self.find_element(MainPageLocators.ORDER_ID_TITLE).is_displayed()

    @allure.step('Получаем номер заказа')
    def get_order_number(self):
        self.wait_for_invisibility_element(MainPageLocators.ORDER_NUMBER_TEXT)
        return self.get_text_for_element(MainPageLocators.ORDER_NUMBER_TEXT)

    @allure.step('Закрываем окно')
    def click_modal_close(self):
        self.wait_for_load_element(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.find_element(MainPageLocators.MODAL_CLOSE_BUTTON).click()