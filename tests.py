from time import sleep

import pytest

from base_class import *
from settings import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#ТC-01 Переход по ссылке "Зарегистрироваться"
def test_register(selenium):
    form = AuthForm(selenium)
    form.register.click()
    sleep(5)

    reset_pass = form.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    assert reset_pass.text == 'Регистрация'


#ТC - 02 Авторизация с валидными данными (телефон + пароль)
def test_positive_by_phone(selenium):
    form = AuthForm(selenium)

    # ввод телефона
    form.username.send_keys(valid_phone)
    form.password.send_keys(valid_pass)
    sleep(5)
    form.btn_click()

    assert form.get_current_url() != '/account_b2c/page'

#ТC-03-авторизация с невалидным номером и паролем
def test_negative_by_phone(selenium, err_mess=None):
    form = AuthForm(selenium)
    form.username.send_keys('+1111111111')
    form.password.send_keys('123_Password')
    sleep(5)
    form.btn_click()

    err_mess = form.driver.find_element(By.ID, 'form-error-message')
    assert err_mess.text == 'Неверный логин или пароль'



# ТC-04 Авторизация с невалидным email
def test_negative_by_email(selenium, err_mess=None):
    form = AuthForm(selenium)
    form.username.send_keys('a1@gg.ww')
    form.password.send_keys('123_Password')
    sleep(15)
    form.btn_click()

    err_mess = form.driver.find_element(By.ID, 'form-error-message')
    assert err_mess.text == 'Неверный логин или пароль'

#ТC-05 Авторизация по email
def test_positive_by_email(selenium):
    form = AuthForm(selenium)
    form.username.send_keys(valid_email)
    form.password.send_keys(valid_pass)
    sleep(5)
    form.btn_click()

    assert form.get_current_url() != '/account_b2c/page'

#TC-06 Проверка перехода по ссылке "Забыл пароль"
def test_forgot_pass(selenium):
    form = AuthForm(selenium)
    form.forgot.click()
    sleep(5)

    reset_pass = form.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    assert reset_pass.text == 'Восстановление пароля'


#TC-07 - проверка перехода по ссылке авторизации пользователя через вконтакте
def test_auth_vk(selenium):
    form = AuthForm(selenium)
    form.vk_btn.click()
    sleep(5)

    assert form.get_base_url() == 'oauth.vk.com'


#TC-08 - проверка перехода по ссылке авторизации пользователя через одноклассники
def test_auth_ok(selenium):
    form = AuthForm(selenium)
    form.ok_btn.click()
    sleep(5)

    assert form.get_base_url() == 'connect.ok.ru'


#TC-09 - проверка перехода по ссылке авторизации пользователя через майлру
def test_auth_mailru(selenium):
    form = AuthForm(selenium)
    form.mailru_btn.click()
    sleep(5)

    assert form.get_base_url() == 'connect.mail.ru'


#TC-10 - проверка перехода по ссылке авторизации пользователя через google
def test_auth_google(selenium):
    form = AuthForm(selenium)
    form.google_btn.click()
    sleep(5)

    assert form.get_base_url() == 'accounts.google.com'


#TC-11 - проверка перехода по ссылке авторизации пользователя через яндекс
def test_auth_ya(selenium):
    form = AuthForm(selenium)
    form.ya_btn.click()
    sleep(5)

    assert form.get_base_url() != 'passport.yandex.ru'


# TC-12 Переключение таба при аутентификации
def test_change_placeholder(selenium):
    form = AuthForm(selenium)
    form.username.send_keys('+79991111111')
    form.password.send_keys('_')
    sleep(5)

    assert form.placeholder.text == 'Мобильный телефон'

    form.username.send_keys(Keys.CONTROL, 'a')
    form.username.send_keys(Keys.DELETE)
    form.username.send_keys('mail@mail.ru')
    form.password.send_keys('_')
    sleep(5)

    assert form.placeholder.text == 'Электронная почта'
    form.username.send_keys(Keys.CONTROL, 'a')
    form.username.send_keys(Keys.DELETE)
    form.username.send_keys('Login')
    form.password.send_keys('_')
    sleep(5)

    assert form.placeholder.text == 'Логин'

# TC-13 Выбор таба по умолчанию
def test_by_phone(selenium):
    form = AuthForm(selenium)

    assert form.placeholder.text == 'Мобильный телефон'

# TC-14 - проверка открытия пользовательского соглашения
def test_agreement(selenium):
    form = AuthForm(selenium)
    original_window = form.driver.current_window_handle
    form.agree.click()
    sleep(5)
    WebDriverWait(form.driver, 5).until(EC.number_of_windows_to_be(2))
    for window_handle in form.driver.window_handles:
        if window_handle != original_window:
            form.driver.switch_to.window(window_handle)
            break
    win_title = form.driver.execute_script("return window.document.title")
    assert win_title == 'User agreement'


#TC-15 Тест на соответствие дизайну страницы авторизации
def test_001_vision(selenium):
    form = AuthForm(selenium)
    form.driver.save_screenshot('screenshot_001.jpg')


