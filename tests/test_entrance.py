import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from curl import *
from locators import Locators
from data import UserData


class TestButtonPersonalAccount:
    def test_entrance_button_personal_account(self, create_driver):
        driver = create_driver
        main_page = main_site

        # на главной странице
        driver.get(main_page)

        # находим и жмем кнопку личный кабинет
        driver.find_element(*Locators.button_personal_account).click()

        # ждем переход на страницу логина
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(login_site))

        # находим и заполняем поле емейл
        driver.find_element(*Locators.field_email).send_keys(UserData.email)

        # находим и заполняем поле пароль
        driver.find_element(*Locators.field_password).send_keys(UserData.password)

        # нажимаем на кнопку войти
        driver.find_element(*Locators.button_entrance).click()

        # ждем переход на главную страницу
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(main_site))

        assert driver.current_url == main_site

class TestButtonEntranceAcc:
    def test_entrance_button_entrance_acc(self, create_driver):
        driver = create_driver
        main_page = main_site

        # на главной странице
        driver.get(main_page)

        # находим и жмем кнопку личный кабинет
        driver.find_element(*Locators.button_entrance_acc).click()

        # ждем переход на страницу логина
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(login_site))

        # находим и заполняем поле емейл
        driver.find_element(*Locators.field_email).send_keys(UserData.email)

        # находим и заполняем поле пароль
        driver.find_element(*Locators.field_password).send_keys(UserData.password)

        # нажимаем на кнопку войти
        driver.find_element(*Locators.button_entrance).click()

        # ждем переход на главную страницу
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(main_site))

        assert driver.current_url == main_site

class TestButtonEntranceTextRegisterPage:
    def test_button_entrance_text_register_page(self, create_driver):
        driver = create_driver
        register_page = register_site

        # на странице регистрации
        driver.get(register_page)

        # находим и жмем на "Войти"
        driver.find_element(*Locators.button_entrance_text).click()

        # ждем переход на страницу логина
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(login_site))

        # находим и заполняем поле емейл
        driver.find_element(*Locators.field_email).send_keys(UserData.email)

        # находим и заполняем поле пароль
        driver.find_element(*Locators.field_password).send_keys(UserData.password)

        # нажимаем на кнопку войти
        driver.find_element(*Locators.button_entrance).click()

        # ждем переход на главную страницу
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(main_site))

        assert driver.current_url == main_site

class TestButtonEntranceTextRecoveryPage:
    def test_button_entrance_text_recovery_page(self, create_driver):
        driver = create_driver
        login_page = login_site

        # на странице входа
        driver.get(login_page)

        # находим и жмем кнопку восстановления пароля
        driver.find_element(*Locators.button_recovery_password).click()

        # ждем переход на страницу восстановления пароля
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(recovery_site))

        # находим и жмем на "Войти"
        driver.find_element(*Locators.button_entrance_text).click()

        # ждем переход на страницу логина
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(login_site))

        # находим и заполняем поле емейл
        driver.find_element(*Locators.field_email).send_keys(UserData.email)

        # находим и заполняем поле пароль
        driver.find_element(*Locators.field_password).send_keys(UserData.password)

        # нажимаем на кнопку войти
        driver.find_element(*Locators.button_entrance).click()

        # ждем переход на главную страницу
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(main_site))

        assert driver.current_url == main_site
