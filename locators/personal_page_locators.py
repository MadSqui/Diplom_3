from selenium.webdriver.common.by import By

class PersonalPageLocators:
    # кнопки
    LOGIN_HEADER = [By.XPATH, "//h2[text()='Вход']"]
    LOGIN_BUTTON = [By.XPATH, "//button[contains(@class, 'button_button_type_primary__1O7Bx')]"]

    # Элементы меню личного кабинета
    ORDER_HISTORY_LINK = [By.XPATH, '//a[text()="История заказов"]']
    LOGOUT_BUTTON = [By.XPATH, './/button[text()="Выход"]']