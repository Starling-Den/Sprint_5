import pytest
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestTitleBread:
    def test_title_bread(self,login_page_enter):
        driver = login_page_enter

        # ждем появление надписи соусы
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.title_sauses))

        # находим и кликаем на соусы
        driver.find_element(*Locators.title_sauses).click()

        # ждем появление надписи булки
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.title_bread))

        # находим и кликаем на булки
        driver.find_element(*Locators.title_bread).click()

        #активная вкладка
        active = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.active_title))

        #ждем загрузку и проверяем, что активна вкладка булки
        assert "Булки" in active.text

class TestTitleSauses:
    def test_title_sauses(self,login_page_enter):
        driver = login_page_enter

        # ждем появление надписи соусы
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.title_sauses))

        # находим и кликаем на соусы
        driver.find_element(*Locators.title_sauses).click()

        #активная вкладка
        active = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.active_title))

        #ждем загрузку и проверяем, что активна вкладка соусы
        assert "Соусы" in active.text

class TestTitleFillings:
    def test_title_fillings(self,login_page_enter):
        driver = login_page_enter

        # ждем появление надписи начинки
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.title_fillings))

        # находим и кликаем на начинки
        driver.find_element(*Locators.title_fillings).click()

        # активная вкладка
        active = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.active_title))

        #ждем загрузку и проверяем, что активна вкладка начинки
        assert "Начинки" in active.text