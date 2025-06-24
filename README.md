ТЕСТЫ:

РЕГИСТРАЦИЯ - находятся в файле test_registration.py:
 - Успешная регистрация (test_new_registration)
 - Регистрация сущ. аккаунта (test_register_exist_acc)
 - Пароль менее 6 символов (test_register_invalid_password)

ВХОД - находятся в файле test_entrance.py:
- Вход через личный кабинет (test_entrance_button_personal_account)
- Вход через кнопку "Войти в аккаунт" (test_entrance_button_entrance_acc)
- Вход через кнопку в форме регистрации (test_button_entrance_text_register_page)
- Вход через кнопку в форме восстановления пароля (test_button_entrance_text_recovery_page)
- Выход из аккаунта (test_button_exit)

ПЕРЕХОДЫ по страницам- находятся в файле test_move_page.py:
- Переход в личный кабинет (test_move_personal_account)
- Переход из личного кабинета в конструктор по клику на конструктор (test_move_to_constructor_from_account)
- Переход из личного кабинета в конструктор по клику на логотип (test_move_to_logotip_from_account)
- Выход из аккаунта (test_exit_personal_account)

ПЕРЕХОДЫ  между разделами в конструкторе- находятся в файле test_move_constructor.py:
- Переход в раздел "Булки" (test_title_bread)
- Переход в раздел "Соусы" (test_title_sauses)
- Переход в раздел "Начинки" (test_title_fillings)

ФИКСТУРЫ

Фикстуры находятся в файле conftest.py:
- Создание драйвера (create_driver)
- Регистрация нового аккаунта (register_new_account)
- Вход в аккаунт (login_page_enter)


ЛОКАТОРЫ

ЛОКАТОРЫ находится в файле locators.py


ДАННЫЕ

Данные находятся в файле data.py