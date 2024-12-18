from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellarBurgersLocators

class TestAuthorization:
# Вход по кнопке «Войти в аккаунт» на главной

    def test_login_main_page(self, driver):
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_NAME).send_keys('alexandrmazin16_478@yandex.ru')
        driver.find_element(*StellarBurgersLocators.PASSWORD_NAME).send_keys('alexandrmazin16')
        driver.find_element(*StellarBurgersLocators.BUTTON_ENTRY).click()
        driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGOUT_BUTTON))
        assert driver.find_element(*StellarBurgersLocators.LOGOUT_BUTTON).text == 'Выход'

# вход через кнопку «Личный кабинет»
    def test_login_personal_account(self, driver):
        driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_NAME).send_keys('alexandrmazin16_478@yandex.ru')
        driver.find_element(*StellarBurgersLocators.PASSWORD_NAME).send_keys('alexandrmazin16')
        driver.find_element(*StellarBurgersLocators.BUTTON_ENTRY).click()
        driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGOUT_BUTTON))
        assert driver.find_element(*StellarBurgersLocators.LOGOUT_BUTTON).text == 'Выход'

# Вход через кнопку в форме регистрации
    def test_login_registration_page(self, driver):
        driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.BUTTON_REGISTRATION).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_REGISTRATION_FORM).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_NAME).send_keys('alexandrmazin16_478@yandex.ru')
        driver.find_element(*StellarBurgersLocators.PASSWORD_NAME).send_keys('alexandrmazin16')
        driver.find_element(*StellarBurgersLocators.BUTTON_ENTRY).click()
        driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGOUT_BUTTON))
        assert driver.find_element(*StellarBurgersLocators.LOGOUT_BUTTON).text == 'Выход'

# Вход через кнопку в форме восстановления пароля
    def test_login_recovery_page(self, driver):
        driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.BUTTON_RECOVERY_PASSWORD).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_RECOVERY_FORM).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_NAME).send_keys('alexandrmazin16_478@yandex.ru')
        driver.find_element(*StellarBurgersLocators.PASSWORD_NAME).send_keys('alexandrmazin16')
        driver.find_element(*StellarBurgersLocators.BUTTON_ENTRY).click()
        driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGOUT_BUTTON))
        assert driver.find_element(*StellarBurgersLocators.LOGOUT_BUTTON).text == 'Выход'