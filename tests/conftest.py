import pytest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from curl import *
from data import UserData
from generators import DataGenerator


@pytest.fixture
def create_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

#используем для теста переходов, тестов констракта
@pytest.fixture
def register_new_account(create_driver):
    driver = create_driver
    register_page = register_site

    # генерируем имя, емейл, пароль
    name = DataGenerator.name_generator()
    email = DataGenerator.email_generator()
    password = DataGenerator.password_generator()

    # открываем страницу для регистрации
    driver.get(register_page)

    # находим и заполняем поле имя
    driver.find_element(*Locators.field_name).send_keys(name)

    # находим и заполняем поле емейл
    driver.find_element(*Locators.field_email).send_keys(email)

    # находим и заполняем поле пароль
    driver.find_element(*Locators.field_password).send_keys(password)

    # нажимаем на кнопку зарегистрироваться
    driver.find_element(*Locators.button_registration).click()

    return driver, email, password

#используем для теста входа
@pytest.fixture
def login_page_enter(create_driver):
    driver = create_driver
    login_page = login_site

    # открываем страницу для входа
    driver.get(login_page)

    # находим и заполняем поле емейл
    driver.find_element(*Locators.field_email).send_keys(UserData.email)

    # находим и заполняем поле пароль
    driver.find_element(*Locators.field_password).send_keys(UserData.password)

    # нажимаем на кнопку войти
    driver.find_element(*Locators.button_entrance).click()

    return driver
