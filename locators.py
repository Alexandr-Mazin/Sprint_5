from selenium.webdriver.common.by import By

class StellarBurgersLocators:
    # Кнопка Войти в аккаунт
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Поле Email на форме входа
    LOGIN_NAME = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]")
    # Поле Пароль в форме входа
    PASSWORD_NAME= (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]")
    # Кнопка Личный кабинет
    ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    # Кнопка Зарегистрироваться
    BUTTON_REGISTRATION = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")
    # Кнопка Войти
    BUTTON_ENTRY = (By.XPATH, "//button[contains(text(),'Войти')]")
    # Кнопка Войти на форме регистрации
    LOGIN_BUTTON_REGISTRATION_FORM = (By.XPATH, "//a[contains(text(),'Войти')]")
    # Кнопка Восстановить пароль
    BUTTON_RECOVERY_PASSWORD = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
    # Кнопка Войти в форме восстановления пароля
    LOGIN_BUTTON_RECOVERY_FORM = (By.XPATH, "//a[contains(text(),'Войти')]")
    # Информация отображаемая после входа в личный кабинет
    IDENTIFICATION_PROFILE = (By.XPATH, "// p[contains(text(), 'В этом разделе вы можете изменить свои персональны')]")
    # Кнопка Конструктор
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    # Информация отображаемая после входа конструктор
    IDENTIFICATION_CONSTRUCTOR = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")
    # Логотип Stellar Burgers
    LOGO_BUTTON = (By.XPATH, "//header/nav[1]/div[1]/a[1]/*[1]")
    # Кнопка Выход
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
    # Информация отображаемая после выхода из аккаунта
    IDENTIFICATION_LOGOUT = (By.XPATH, "//h2[contains(text(),'Вход')]")
    # раздел конструктора булки
    BUNS_SECTION = (By.XPATH, "//span[contains(text(),'Булки')]")
    # раздел конструктора соусы
    SAUCES_SECTION = (By.XPATH, "//span[contains(text(),'Соусы')]")
    # раздел конструктора Начинки
    FILLINGS_SECTION = (By.XPATH, "//span[contains(text(),'Начинки')]")
    # Поле Имя на форме регистрации
    REGISTRATION_NAME = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]")
    # Поле Email на форме регистрации
    REGISTRATION_EMAIL = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]")
    # Поле Пароль на форме регистрации
    REGISTRATION_PASSWORD = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]")
    # Кнопка Зарегистрироваться на форме регистрации
    BUTTON_REGISTRATION_USER = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    # Соощение Некорректный пароль
    WRONG_PASSWORD = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")
    # Класс выбранного раздела соусы
    ACTIVATED_SECTION_SAUCES = (By.XPATH, "//body/div/div/main/section/div/div[2]")
    # Класс выбранного раздела булки
    ACTIVATED_SECTION_BUNS = (By.XPATH,"//body/div/div/main/section/div/div[1]")
    # Класс выбранного раздела начинки
    ACTIVATED_SECTION_FILLINGS = (By.XPATH,"//body/div/div/main/section/div/div[3]")
