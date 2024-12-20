from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellarBurgersLocators
import random

class TestRegistration:
# Регистрация

    def test_registration(self, driver):
        random_number = random.randint(100, 999)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.BUTTON_REGISTRATION).click()
        driver.find_element(*StellarBurgersLocators.REGISTRATION_NAME).send_keys(f'alexandrmazin16_{random_number}@yandex.ru')
        driver.find_element(*StellarBurgersLocators.REGISTRATION_EMAIL).send_keys(f'alexandrmazin16_{random_number}@yandex.ru')
        driver.find_element(*StellarBurgersLocators.REGISTRATION_PASSWORD).send_keys(f'alexandrmazin16{random_number}')
        driver.find_element(*StellarBurgersLocators.BUTTON_REGISTRATION_USER).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUTTON_ENTRY))
        driver.find_element(*StellarBurgersLocators.LOGIN_NAME).send_keys(f'alexandrmazin16_{random_number}@yandex.ru')
        driver.find_element(*StellarBurgersLocators.PASSWORD_NAME).send_keys(f'alexandrmazin16{random_number}')
        driver.find_element(*StellarBurgersLocators.BUTTON_ENTRY).click()
        driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGOUT_BUTTON))
        assert driver.find_element(*StellarBurgersLocators.LOGOUT_BUTTON).text == 'Выход'

    def test_registration_failed(self, driver):
        random_number = random.randint(100, 999)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.BUTTON_REGISTRATION).click()
        driver.find_element(*StellarBurgersLocators.REGISTRATION_NAME).send_keys(f'alexandrmazin16_{random_number}@yandex.ru')
        driver.find_element(*StellarBurgersLocators.REGISTRATION_EMAIL).send_keys(f'alexandrmazin16_{random_number}@yandex.ru')
        driver.find_element(*StellarBurgersLocators.REGISTRATION_PASSWORD).send_keys(f'1{random_number}')
        driver.find_element(*StellarBurgersLocators.BUTTON_REGISTRATION_USER).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.WRONG_PASSWORD))
        assert driver.find_element(*StellarBurgersLocators.WRONG_PASSWORD).text == 'Некорректный пароль'