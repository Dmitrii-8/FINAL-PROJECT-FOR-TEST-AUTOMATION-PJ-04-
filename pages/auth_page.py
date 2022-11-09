from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://b2c.passport.rt.ru'

        super().__init__(web_driver, url)

    phone = WebElement(id='username')
    password = WebElement(id='password')
    registration_link = WebElement(id='kc-register')
    btn_login = WebElement(id='kc-login')
    auth_title = WebElement(xpath='//*[@id="page-right"]/div/div/h1')
    phone_tab = WebElement(id='t-btn-tab-phone')
    logo_lk = WebElement(xpath='//*[@id="page-left"]/div/div[2]/h2')
    auth_form = WebElement(xpath='//*[@id="page-left"]/div/div')
    lk_form = WebElement(xpath='//*[@id="page-right"]/div/div[2]')
    message_invalid_username_or_password = WebElement(xpath='//*[@id="page-right"]/div/div/p')
    the_element_forgot_the_password = WebElement(xpath='//*[@id="forgot_password"]')
