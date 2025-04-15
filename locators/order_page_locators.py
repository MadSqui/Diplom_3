from selenium.webdriver.common.by import By

class OrderPageLocators:

    # Общие элементы заказов
    ORDER_ITEM = [By.XPATH, './/li[contains(@class, "OrderHistory_listItem")]']
    LAST_ORDER_NUMBER = [By.XPATH, '//li[1]//p[@class="text text_type_digits-default"]']

    # Модальное окно заказа
    ORDER_MODAL = [By.XPATH, './/div[contains(@class, "Modal_orderBox")]']

    # Статистика заказов
    TOTAL_ORDERS_COUNT = [By.XPATH,
                          '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class, "digits-large")]']
    TODAY_ORDERS_COUNT = [By.XPATH,
                          './/p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class, "digits-large")]']

    # Лента заказов в работе
    ORDERS_IN_PROGRESS = [By.XPATH, './/*[contains(@class, "orderListReady")]//li[contains(@class,"digits-default")]']