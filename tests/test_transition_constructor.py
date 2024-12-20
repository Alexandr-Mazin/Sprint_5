from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellarBurgersLocators

class TestTransitionPersonalAccount:
# Переход из личного кабинета в конструктор

    def test_transition_constructor(self, driver):
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_NAME).send_keys('alexandrmazin16_478@yandex.ru')
        driver.find_element(*StellarBurgersLocators.PASSWORD_NAME).send_keys('alexandrmazin16')
        driver.find_element(*StellarBurgersLocators.BUTTON_ENTRY).click()
        driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_CONSTRUCTOR))
        driver.find_element(*StellarBurgersLocators.BUTTON_CONSTRUCTOR).click()
        profile = driver.find_element(*StellarBurgersLocators.IDENTIFICATION_CONSTRUCTOR).text
        assert 'Соберите бургер' in profile


    def test_transition_logo(self, driver):
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_NAME).send_keys('alexandrmazin16_478@yandex.ru')
        driver.find_element(*StellarBurgersLocators.PASSWORD_NAME).send_keys('alexandrmazin16')
        driver.find_element(*StellarBurgersLocators.BUTTON_ENTRY).click()
        driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.LOGO_BUTTON))
        driver.find_element(*StellarBurgersLocators.LOGO_BUTTON).click()
        profile = driver.find_element(*StellarBurgersLocators.IDENTIFICATION_CONSTRUCTOR).text
        assert 'Соберите бургер' in profile