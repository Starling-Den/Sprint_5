import pytest
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from curl import *


class TestSwitchPersonalAccount:
    def test_move_personal_account(self, login_page_enter):
        driver = login_page_enter

        #находим и кликаем на кнопку личный кабинет
        driver.find_element(*Locators.button_personal_account).click()

        #ждем переход на страницу аккаунта
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(account_site))

        #проверяем, что находимся на странице аккаунта
        assert driver.current_url == account_site

class TestSwitchConstructor:
    def test_move_to_constructor_from_account(self, login_page_enter):

        driver = login_page_enter

        # ждем переход на главную страницу
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(main_site))

        # находим и кликаем на кнопку личный кабинет
        driver.find_element(*Locators.button_personal_account).click()

        # ждем появление надписи конструктор
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.button_construction_acc))

        # находим и кликаем на кнопку конструктор
        driver.find_element(*Locators.button_construction_acc).click()

        # ждем переход на главную страницу
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(main_site))

        assert driver.current_url == main_site

class TestSwitchLogotip:
    def test_move_to_logotip_from_account(self, login_page_enter):
        driver = login_page_enter

        # ждем переход на главную страницу
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(main_site))

        # находим и кликаем на кнопку личный кабинет
        driver.find_element(*Locators.button_personal_account).click()

        # ждем появление логотипа
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.logotip_acc))

        # находим и кликаем на логотип
        driver.find_element(*Locators.logotip_acc).click()

        # ждем переход на главную страницу
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(main_site))

        assert driver.current_url == main_site
        
class TestExitAccount:
    def test_exit_personal_account(self, login_page_enter):
        driver = login_page_enter

        # ждем переход на главную страницу
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(main_site))

        # находим и кликаем на кнопку личный кабинет
        driver.find_element(*Locators.button_personal_account).click()

        # ждем появление кнопки выход
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.button_exit))

        # находим и кликаем на кнопку выход
        driver.find_element(*Locators.button_exit).click()

        # ждем переход на страницу логина
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(login_site))

        assert driver.current_url == login_site
