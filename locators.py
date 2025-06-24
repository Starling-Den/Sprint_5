from selenium.webdriver.common.by import By


class Locators:
    # кнопка личный кабинет
    button_personal_account = (By.XPATH, ".//a[@href='/account']")

    # кнопка войти в аккаунт
    button_entrance_acc = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")

    # кнопка конструктор на главной стр
    button_construction = (
    By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo']")

    # логотип
    logotip = (By.XPATH, ".//a[(@href='/') and (@class='active')]")

    #логотип из акка
    logotip_acc = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")

    # вкладка булки
    title_bread = (By.XPATH, ".//span[contains(text(), 'Булки')]")

    # вкладка Соусы
    title_sauses = (By.XPATH, ".//span[contains(text(), 'Соусы')]")

    # вкладка начинки
    title_fillings = (By.XPATH, ".//span[contains(text(), 'Начинки')]")

    # активная вкладка
    active_title = (
    By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")

    # поле емейл
    field_email = (By.XPATH, ".//div[label[contains(text(), 'Email')]]//input")

    # поле пароль
    field_password = (By.XPATH, ".//div[label[contains(text(), 'Пароль')]]//input")

    # поле имя
    field_name = (By.XPATH, ".//div[label[contains(text(), 'Имя')]]//input")

    # кнопка войти в логине
    button_entrance = (By.XPATH, ".//button[contains(text(), 'Войти')]")

    # кнопка войти на форме странице регистрации
    button_entrance_text = (By.XPATH, ".//a[@href='/login']")

    # кнопка зарегистрироваться
    button_registration = (By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]")

    # кнопка выход
    button_exit = (By.XPATH, ".//button[contains(text(), 'Выход')]")

    # кнопка восстановления пароля
    button_recovery_password = (By.XPATH, ".//a[@href='/forgot-password']")

    #надпись зарегистрироваться
    button_registration_text = (By.XPATH, ".//a[@href='/register']")

    #надпись такой пользователь уже существует
    text_error = (By.XPATH, ".//p[@class='input__error text_type_main-default']")

    #кнопка конструктор в акке
    button_construction_acc = (By.XPATH, ".//p[contains(text(), 'Конструктор')]")
