from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellarBurgersLocators

class TestTransitionPersonalAccount:
# Переход в личный кабинет

    def test_login_personal_account(self, driver):
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_NAME).send_keys('alexandrmazin16_478@yandex.ru')
        driver.find_element(*StellarBurgersLocators.PASSWORD_NAME).send_keys('alexandrmazin16')
        driver.find_element(*StellarBurgersLocators.BUTTON_ENTRY).click()
        driver.find_element(*StellarBurgersLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGOUT_BUTTON))
        profile = driver.find_element(*StellarBurgersLocators.IDENTIFICATION_PROFILE).text
        assert 'В этом разделе вы можете изменить свои персональны' in profile
