from selenium.webdriver.common.by import By

class PasswordPageLocators:

    # Ссылки
    PASSWORD_RECOVERY_LINK = [By.XPATH, './/a[text()="Восстановить пароль"]']

    # Кнопки
    RECOVER_BUTTON = [By.XPATH, "//button[contains(@class, 'button_button_type_primary__1O7Bx')]"]
    SHOW_PASSWORD_BUTTON = [By.XPATH, '//div[contains(@class, "input__icon-action")]']
    HIDE_PASSWORD_BUTTON = [By.XPATH, '//label[text()="Пароль"]/parent::div']

    # Поля ввода
    RECOVERY_EMAIL_INPUT = [By.XPATH, '//label[text()="Email"]/following-sibling::input']
    NEW_PASSWORD_INPUT = [By.XPATH, '//label[text()="Пароль"]/following-sibling::input']