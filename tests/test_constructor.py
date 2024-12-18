from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellarBurgersLocators

class TestTransitionPersonalAccount:
# работают переходы к разделам: «Булки»

    def test_transition_constructor_buns(self, driver):
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_NAME).send_keys('alexandrmazin16_478@yandex.ru')
        driver.find_element(*StellarBurgersLocators.PASSWORD_NAME).send_keys('alexandrmazin16')
        driver.find_element(*StellarBurgersLocators.BUTTON_ENTRY).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.SAUCES_SECTION))
        driver.find_element(*StellarBurgersLocators.SAUCES_SECTION).click()
        driver.find_element(*StellarBurgersLocators.BUNS_SECTION).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.BUNS_SECTION))

        expected_class = driver.find_element(*StellarBurgersLocators.ACTIVATED_SECTION_BUNS).get_attribute('class')

        assert "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect" in expected_class

    def test_transition_constructor_sauces(self, driver):
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_NAME).send_keys('alexandrmazin16_478@yandex.ru')
        driver.find_element(*StellarBurgersLocators.PASSWORD_NAME).send_keys('alexandrmazin16')
        driver.find_element(*StellarBurgersLocators.BUTTON_ENTRY).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.SAUCES_SECTION))
        driver.find_element(*StellarBurgersLocators.SAUCES_SECTION).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.SAUCES_SECTION))

        expected_class = driver.find_element(*StellarBurgersLocators.ACTIVATED_SECTION_SAUCES).get_attribute('class')

        assert "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect" in expected_class

    def test_transition_constructor_fillings(self, driver):
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_NAME).send_keys('alexandrmazin16_478@yandex.ru')
        driver.find_element(*StellarBurgersLocators.PASSWORD_NAME).send_keys('alexandrmazin16')
        driver.find_element(*StellarBurgersLocators.BUTTON_ENTRY).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.SAUCES_SECTION))
        driver.find_element(*StellarBurgersLocators.FILLINGS_SECTION).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.FILLINGS_SECTION))

        expected_class = driver.find_element(*StellarBurgersLocators.ACTIVATED_SECTION_FILLINGS).get_attribute('class')

        assert "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect" in expected_class

