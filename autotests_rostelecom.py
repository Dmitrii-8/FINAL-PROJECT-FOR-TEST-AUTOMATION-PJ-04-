import pytest
import time

from pages.auth_page import AuthPage
from pages.registration_page import RegPage

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By


# Test-Case №1
# Корректное отображение страницы авторизации:
def test_start_page_is_correct(web_browser):
    page = AuthPage(web_browser)
    phone_tab_class = page.phone_tab.get_attribute("class")
    assert phone_tab_class == "rt-tab rt-tab--active"
    assert page.phone.is_clickable()
    assert page.password.is_clickable()
    assert page.btn_login.is_clickable()
    assert page.registration_link.is_clickable()
    assert page.auth_title.get_text() == "Авторизация"
    assert page.logo_lk.get_text() == "Личный кабинет"

# Test-Case №2
# Проверка наличия и корректного отображения кнопок и элементов на странице:
def test_the_presence_of_buttons_and_elements_on_the_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(9)
    driver.get("https://b2c.passport.rt.ru/")

    # Проверка наличия и отображения кнопки "Войти":
    try:
        button = driver.find_element(By.NAME, "login")
        print(button)
        print("Элемент 1 найден")
    except NoSuchElementException:
        print("Элемент 1 не найден!")

    # Проверка наличия элемента "Телефон" в меню аутентификации:
    try:
        telephone = driver.find_element(By.XPATH,
                                        "/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/div[1]")
        print(telephone)
        print("Элемент 2 найден")
    except NoSuchElementException:
        print("Элемент 2 не найден!")
    # Проверка наличия элемента "Почта" в меню:
    try:
        letter = driver.find_element(By.ID, "t-btn-tab-mail")
        print(letter)
        print("Элемент 3 найден")
    except NoSuchElementException:
        print("Элемент 3 не найден!")

    # Проверка наличия элемента "Логин":
    try:
        log_in = driver.find_element(By.ID, "t-btn-tab-login")
        print(log_in)
        print("Элемент 4 найден")
    except NoSuchElementException:
        print("Элемент 4 не найден!")

    # Проверка наличия элемента "Лицевой счет":
    try:
        litsevoy_account = driver.find_element(By.CSS_SELECTOR, "#t-btn-tab-ls")
        print(litsevoy_account)
        print("Элемент 5 найден")
    except NoSuchElementException:
        print("Элемент 5 не найден!")

    # Проверка наличия логотипа:
    try:
        logo = driver.find_element(By.CLASS_NAME, "what-is-container__logo-container")
        print(logo)
        print("Элемент 6 найден")
    except NoSuchElementException:
        print("Элемент 6 не найден!")

    # Проверка наличия номера горячей линии службы поддержки:
    try:
        text = driver.find_element(By.LINK_TEXT, "8 800 100 0 800")
        print(text)
        print("Элемент 7 найден")
    except NoSuchElementException:
        print("Элемент 7 не найден!")

    # Проверка вертикального разделения на два блока:
    try:
        block_left = driver.find_element(By.ID, "page-left")
        print(block_left)
        block_right = driver.find_element(By.ID, "page-right")
        print(block_right)

        print("Форма 'Авторизация' вертикально разделена на два блока!")

    except NoSuchElementException:
        print("Вертикальное разделение на блоки отсутствует!")


# Test-Case №3 (FB-01)
# Проверка наличия элементов, как в левом так и в правом блоках страницы:
@pytest.mark.xfail(reason="Расположение элементов на странице не соответсвует ожидаемым требованиям")
def test_location_of_page_blocks(web_browser):
    page = AuthPage(web_browser)
    assert page.auth_form.find(timeout=1)
    assert page.lk_form.find(timeout=1)


# Test-Case №4 (FB-02)
# Проверка в форме регистрации правильной работы кнопки "Продолжить"
@pytest.mark.xfail(reason="Требования к кнопке: имется текст 'Продолжить'")
def test_registration_page_and_continue_button(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    assert reg_page.name_field_text.get_text() == "Имя"
    assert reg_page.last_name_field_text.get_text() == "Фамилия"
    assert reg_page.region_field_text.get_text() == "Регион"
    assert reg_page.email_or_mobile_phone_field_text.get_text() == "E-mail или Мобильный телефон"
    assert reg_page.password_field_text.get_text() == "Пароль"
    assert reg_page.password_confirmation_field_text.get_text() == "Подтверждение пароля"
    assert reg_page.continue_button.get_text() == "Продолжить"


# Test-Case №5
# Негативный тест. Некорректный ввод значения в поле "Имя" более двух символов при регистрации пользователя
# Последующее появление текста-подсказки об ошибке:
def test_registration_with_an_incorrect_value_in_the_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('X')
    reg_page.last_name_field.send_keys("Фамилия")
    reg_page.email_or_mobile_phone_field.send_keys("random5678@mail.ru")
    reg_page.password_field.send_keys("789rtfgHB")
    reg_page.password_confirmation_field.send_keys("789rtfgHB")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Поле заполняется кириллицей от 2 до 30 символов!"

# Test-Case №6 (FB-03)
# Тест названия таб выбора "Номер"
@pytest.mark.xfail(reason="Не соответсвует ожидаемым требованиям Таб выбора 'Номер' ")
def test_phone_tab(web_browser):
    page = AuthPage(web_browser)
    assert page.phone_tab.get_text() == "Номер"



# Test-Case №7
# Негативный тест. Некорректный ввод значения в поле "Фамилия" более тридцати символов, при регистрации пользователя
# Последующее появление текста-подсказки об ошибке:
def test_registration_with_an_incorrect_value_in_the_last_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Сергей")
    reg_page.last_name_field.send_keys("вводимвполебольшетридцатисимволов")
    reg_page.email_or_mobile_phone_field.send_keys("random5678@mail.ru")
    reg_page.password_field.send_keys("789rtfgHB")
    reg_page.password_confirmation_field.send_keys("789rtfgHB")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_last_name.get_text() == "Поле заполняется кириллицей от 2 до 30 символов!"

# Test-Case №8
# Проверка регистрации пользов.с незаполненным полем "имя", с последующим появлением текста-подсказки об ошибке:
def test_registration_page_with_empty_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('')
    reg_page.last_name_field.send_keys("Фамилия")
    reg_page.email_or_mobile_phone_field.send_keys("random5678@mail.ru")
    reg_page.password_field.send_keys("789rtfgHB")
    reg_page.password_confirmation_field.send_keys("789rtfgHB")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Поле заполняется кириллицей от 2 до 30 символов!"

# Test-Case №9
# Негативный тест. Пользовательская регистрация с использованием зарегестрированного номера
# Отображение оповещеня об этом:
def test_registration_of_an_already_registered_user(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Ванек")
    reg_page.last_name_field.send_keys("Лысый")
    reg_page.email_or_mobile_phone_field.send_keys("+7929325****") #последние 4 цифры номера при проведении теста не скрывались!
    reg_page.password_field.send_keys("Random987654")
    reg_page.password_confirmation_field.send_keys("Random987654")
    reg_page.continue_button.click()
    assert reg_page.notification_form.is_visible

# Test-Case №10
# Тестирование аутентификации зарегестрированного пользователя:
def test_authorisation_valid(web_browser):
    page = AuthPage(web_browser)
    page.phone.send_keys("+7929325****") #!!!последние 4 цифры номера при проведении теста не скрывались!
    page.password.send_keys("Random987654")
    page.btn_login.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url() \
           and '&client_id=account_b2c#/' in page.get_current_url()

# Test-Case №11
# Checking the presence and clickability of the "Support", "Write", "X" buttons,
# as well as closing the opened form:
def testing():
   #pytest.driver = webdriver.Chrome("C:/chromedriver.exe")
   driver = webdriver.Chrome()
   driver.maximize_window()
   driver.implicitly_wait(9)
   driver.get("https://b2c.passport.rt.ru/")

   # Проверка корректного отображения и кликабелбности элемента "Поддержка":
   try:
       #text_support = driver.find_element(By.LINK_TEXT, "Поддержка")
       #print(text_support)
       support = driver.find_element(By.ID, "widget_bar").click()
       print(support)
       print("Item 9 found!")

       # Проверка корректного отображения и кликабельности кнопки "Написать"
       try:
           elemetr = driver.find_element(By.ID, "widget_sendPrechat").click()
           print(elemetr)
           print("Item 10 found!")
       except NoSuchElementException:
           print("Item 10 not found!")

       # Проверка отображения и кликабельности кнопки "X":
       try:
           close = driver.find_element(By.ID, "widget_closeChat").click()
           print(close)
           print('Кнопка отображается!')
           time.sleep(3)

           try:
               cclose = driver.find_element(By.ID, "widget_closeChat")
               print('Кнопка закрытия неисправна!')
           except NoSuchElementException:
               print("Сlose button found!")

       except NoSuchElementException:
           print("Кнопка отсутствует!")

   except NoSuchElementException:
       print("Item 9 not found!")

   # Проверка наличия элемента "ok":
   try:
       ok_niki = driver.find_element(By.ID, "oidc_ok").click()
       time.sleep(1)
       print(ok_niki)
       print("Item ok found!")

   except NoSuchElementException:
        print("Item 'ok' found!")

   # Проверка наличия элемента "vk":
   try:
       driver.get("https://b2c.passport.rt.ru/")
       time.sleep(1)
       vk_te = driver.find_element(By.ID, "oidc_vk").click()
       time.sleep(1)
       print("Item 'vk' found!")

   except NoSuchElementException:
        print("Item 'vk' not found!")

   try:
       # Проверка наличия и кликабельности кнопки "Мой мир"
       driver.get("https://b2c.passport.rt.ru/")
       time.sleep(1)
       my_world = driver.find_element(By.ID, "oidc_mail").click()
       time.sleep(1)
       print("Item 'my_world' found!")

   except NoSuchElementException:
       print("Item 'my_world' not found!")
   # yield

# Test-Case №12 (FB-04)
# Подробный тест кнопки закрытия окна - "X"
@pytest.mark.xfail(reason="Имеется кнопка 'X' закрыть ")
def test_notification_form(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Валера")
    reg_page.last_name_field.send_keys("Скромный")
    reg_page.email_or_mobile_phone_field.send_keys("+7929325****") #последние 4 цифры номера при проведении теста не скрывались!
    reg_page.password_field.send_keys("Random987654")
    reg_page.password_confirmation_field.send_keys("Random987654")
    reg_page.continue_button.click()
    assert reg_page.login_button.get_text() == 'Войти'
    assert reg_page.recover_password_button.get_text() == 'Восстановить пароль'
    assert reg_page.close_button.get_text() == 'X'



# Test-Case №13
# Вход зарегистрированного пользователя с неправильным паролем в форме "Авторизация"
# "Забыл пароль" меняет цвет на оранж.:
def test_authorization_of_a_user_with_an_invalid_password(web_browser):
    page = AuthPage(web_browser)
    page.phone.send_keys('+7929325****') #!!!последние 4 цифры номера при проведении теста не скрывались!
    page.password.send_keys("Forgot")
    page.btn_login.click()
    assert page.message_invalid_username_or_password.get_text() == "Неверный логин или пароль"
    assert "rt-link--orange" in page.the_element_forgot_the_password.get_attribute('class')


# Test-Case №14
# При регистрации нового пользователя, в поле ввода "Фамилия" вместо кириллицы,
# недопустимые символы (форма "Регистрации"):

def test_instead_of_cyrillic_invalid_characters(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Леонид")
    reg_page.last_name_field.send_keys("№*@!")
    reg_page.email_or_mobile_phone_field.send_keys("random5678@mail.ru")
    reg_page.password_field.send_keys("Random987654")
    reg_page.password_confirmation_field.send_keys("Random987654")
    reg_page.continue_button.click()
    assert reg_page.message_must_be_filled_in_cyrillic.get_text() == "Поле заполняется кириллицей от 2 до 30 символов!"

# Test-Case №15
# Email в поле ввода невалидный (Email или мобильный телефон):
def test_invalid_email_or_mobile_phone(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Владимир")
    reg_page.last_name_field.send_keys("Фамилия")
    reg_page.email_or_mobile_phone_field.send_keys("987654321")
    reg_page.password_field.send_keys("Random987654")
    reg_page.password_confirmation_field.send_keys("Random987654")
    reg_page.continue_button.click()
    assert reg_page.message_enter_the_phone_in_the_format.get_text() == "Введите телефон в формате +7ХХХХХХХХХХ или" \
                                                                        " +375XXXXXXXXX, или email в формате example@email.ru"

# Test-Case №16
# При регистрации нового пользователя пароль состоит меньше чем из восьми символов,
# Последующее появление текста-подсказки об ошибке:
def test_incorrect_password_during_registration(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Искандер")
    reg_page.last_name_field.send_keys("Двурогий")
    reg_page.email_or_mobile_phone_field.send_keys("random5678@mail.ru")
    reg_page.password_field.send_keys("12qw")
    reg_page.password_confirmation_field.send_keys("12qw")
    reg_page.continue_button.click()
    assert reg_page.error_message_password.get_text() == "Пароль состоит не менее чем из 8 символов!"

# Test-Caseс №17
# Не совпадают поля ввода "Пароль" и "Подтверждение пароля"  в форме "Регистрация":
def test_password_and_password_confirmation_do_not_match(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Владимир")
    reg_page.last_name_field.send_keys("Фамилия")
    reg_page.email_or_mobile_phone_field.send_keys("random5678@mail.ru")
    reg_page.password_field.send_keys("Random987654")
    reg_page.password_confirmation_field.send_keys("random12345")
    reg_page.continue_button.click()
    assert reg_page.message_passwords_dont_match.get_text() == "Пароли не совпадают"




