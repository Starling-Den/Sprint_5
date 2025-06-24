import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from data import UserData
from curl import *
from time import sleep

class TestRegister:
    def test_new_registration(self, register_new_account):
        driver, email, password = register_new_account

        # ждем переход на cтраницу логина
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(login_site))

        # находим и заполняем поле емейл
        driver.find_element(*Locators.field_email).send_keys(email)

        # находим и заполняем поле пароль
        driver.find_element(*Locators.field_password).send_keys(password)

        # нажимаем на кнопку войти
        driver.find_element(*Locators.button_entrance).click()

        # ждем переход на главную страницу
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(main_site))

        assert driver.current_url == main_site

#для прохождения теста нужно иметь ранее зареганный акк (UserData)
class TestRegisterExistAcc:
    def test_register_exist_acc(self, create_driver):
        driver = create_driver
        login_page = login_site

        #на страницу логина
        driver.get(login_page)

        # находим и жмем на "Зарегистрироваться"
        driver.find_element(*Locators.button_registration_text).click()

        # ждем переход на cтраницу регистрации
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(register_site))

        # находим и заполняем поле имя
        driver.find_element(*Locators.field_name).send_keys(UserData.name)

        # находим и заполняем поле емейл
        driver.find_element(*Locators.field_email).send_keys(UserData.email)

        # находим и заполняем поле пароль
        driver.find_element(*Locators.field_password).send_keys(UserData.password)

        # нажимаем на кнопку зарегистрироваться
        driver.find_element(*Locators.button_registration).click()

        # ждем ошибку
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.text_error))

class TestInvalidPassword:
    def test_register_invalid_password(self, create_driver):
        driver = create_driver

        login_page = login_site

        # на страницу логина
        driver.get(login_page)

        # находим и жмем на "Зарегистрироваться"
        driver.find_element(*Locators.button_registration_text).click()

        # ждем переход на cтраницу регистрации
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(register_site))

        # находим и заполняем поле имя
        driver.find_element(*Locators.field_name).send_keys(UserData.name)

        # находим и заполняем поле емейл
        driver.find_element(*Locators.field_email).send_keys(UserData.email)

        # находим и заполняем поле пароль
        driver.find_element(*Locators.field_password).send_keys(UserData.invalid_password)

        # нажимаем на кнопку зарегистрироваться
        driver.find_element(*Locators.button_registration).click()

        # ждем ошибку
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.text_error))
