from selenium.webdriver.common.by import By

class MainPageLocators:
        # Основные элементы
        CONSTRUCTOR_BUTTON = [By.XPATH, '//p[text()="Конструктор"]']
        ORDER_FEED_BUTTON = [By.XPATH, '//p[text()="Лента Заказов"]']
        PERSONAL_ACCOUNT_BUTTON = [By.XPATH, '//p[text()="Личный Кабинет"]']

        # Элементы конструктора бургеров
        INGREDIENT_IMAGE = [By.XPATH, '(//img[@class="BurgerIngredient_ingredient__image__3e-07 ml-4 mr-4"])[1]']
        INGREDIENT_DETAILS_MODAL_TITLE = [By.XPATH, '//h2[text()="Детали ингредиента"]']
        MODAL_CLOSE_BUTTON = [By.XPATH, '//button[contains(@class, "modal__close")]']
        BURGER_CONSTRUCTOR_TITLE = [By.XPATH, '//h1[contains(@class, "text_type_main-large")]']
        BASKET_SECTION = [By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]']
        BUN_COUNTER = [By.XPATH, '(//p[contains(@class, "counter_counter__num__3nue1")])[1]']
        PLACE_ORDER_BUTTON = [By.XPATH, '//button[contains(@class, "button_button_type_primary__1O7Bx")]']

        # Модальное окно заказа
        ORDER_ID_TITLE = [By.XPATH, '//p[text()="идентификатор заказа"]']
        ORDER_NUMBER_TEXT = [By.CSS_SELECTOR, '.Modal_modal__loading__3534A']

        # Форма авторизации
        EMAIL_INPUT = [By.XPATH, '//label[text()="Email"]/following-sibling::input']
        PASSWORD_INPUT = [By.XPATH, '//label[text()="Пароль"]/following-sibling::input']