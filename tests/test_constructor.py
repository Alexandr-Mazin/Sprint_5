from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellarBurgersLocators

class TestTransitionPersonalAccount:
# работают переходы к разделам

    def test_transition_constructor_buns(self, driver):
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_NAME).send_keys('alexandrmazin16_478@yandex.ru')
        driver.find_element(*StellarBurgersLocators.PASSWORD_NAME).send_keys('alexandrmazin16')
        driver.find_element(*StellarBurgersLocators.BUTTON_ENTRY).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUNS_SECTION))

        element_sauces = driver.find_element(*StellarBurgersLocators.ACTIVATED_SECTION_BUNS)
        assert "tab_tab_type_current__2BEPc" in element_sauces.get_attribute('class')

    def test_transition_constructor_sauces(self, driver):
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_NAME).send_keys('alexandrmazin16_478@yandex.ru')
        driver.find_element(*StellarBurgersLocators.PASSWORD_NAME).send_keys('alexandrmazin16')
        driver.find_element(*StellarBurgersLocators.BUTTON_ENTRY).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.SAUCES_SECTION))
        driver.find_element(*StellarBurgersLocators.SAUCES_SECTION).click()

        element_sauces = driver.find_element(*StellarBurgersLocators.ACTIVATED_SECTION_SAUCES)
        assert "tab_tab_type_current__2BEPc" in element_sauces.get_attribute('class')

    def test_transition_constructor_fillings(self, driver):
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_NAME).send_keys('alexandrmazin16_478@yandex.ru')
        driver.find_element(*StellarBurgersLocators.PASSWORD_NAME).send_keys('alexandrmazin16')
        driver.find_element(*StellarBurgersLocators.BUTTON_ENTRY).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.FILLINGS_SECTION))
        driver.find_element(*StellarBurgersLocators.FILLINGS_SECTION).click()

        element_fillings = driver.find_element(*StellarBurgersLocators.ACTIVATED_SECTION_FILLINGS)
        assert "tab_tab_type_current__2BEPc" in element_fillings.get_attribute('class')

