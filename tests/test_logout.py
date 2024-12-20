from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellarBurgersLocators

class TestLogoutPersonalAccount:
# Выход из аккаунта

    def test_logout_account(self, driver):
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_NAME).send_keys('alexandrmazin16_478@yandex.ru')
        driver.find_element(*StellarBurgersLocators.PASSWORD_NAME).send_keys('alexandrmazin16')
        driver.find_element(*StellarBurgersLocators.BUTTON_ENTRY).click()
        driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.LOGOUT_BUTTON))
        driver.find_element(*StellarBurgersLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_ENTRY))
        assert driver.find_element(*StellarBurgersLocators.IDENTIFICATION_LOGOUT).text == 'Вход'