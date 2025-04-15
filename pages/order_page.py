import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):

    @allure.step('Клик на заказ')
    def click_order(self):
        self.wait_for_load_element(OrderPageLocators.ORDER_ITEM)
        self.find_element(OrderPageLocators.ORDER_ITEM).click()

    @allure.step('Отображение окна с деталями заказа')
    def order_modal_is_displayed(self):
        return self.find_element(OrderPageLocators.ORDER_MODAL).is_displayed()

    @allure.step('Получить номер последнего заказа')
    def get_last_order_number(self):
        self.wait_for_load_element(OrderPageLocators.LAST_ORDER_NUMBER)
        return self.get_text_for_element(OrderPageLocators.LAST_ORDER_NUMBER)

    @allure.step('Количество заказов за все время')
    def get_count_all_orders(self):
        self.wait_for_load_element(OrderPageLocators.TOTAL_ORDERS_COUNT)
        return self.get_text_for_element(OrderPageLocators.TOTAL_ORDERS_COUNT)

    @allure.step('Количество заказов за сегодня')
    def get_count_today_orders(self):
        self.wait_for_load_element(OrderPageLocators.TODAY_ORDERS_COUNT)
        return self.get_text_for_element(OrderPageLocators.TODAY_ORDERS_COUNT)

    @allure.step('Получить номер заказа "В работе"')
    def get_order_in_work(self):
        self.wait_for_load_element(OrderPageLocators.ORDERS_IN_PROGRESS)
        return self.get_text_for_element(OrderPageLocators.ORDERS_IN_PROGRESS)