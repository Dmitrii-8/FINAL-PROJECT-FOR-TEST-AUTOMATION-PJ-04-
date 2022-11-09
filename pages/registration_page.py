from pages.elements import WebElement
from pages.base import WebPage

class RegPage(WebPage):

    def __init__(self, web_driver, url):
        super().__init__(web_driver, url)

    name_field_text = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/span[2]')
    continue_button = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/button')
    last_name_field_text = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    email_or_mobile_phone_field_text = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[3]/div/span[2]')
    region_field_text = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[2]/div/div/span[2]')

    password_field_text = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/div/span[2]')
    password_confirmation_field_text = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/div/span[2]')


    name_field = WebElement (xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input')
    last_name_field = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input')
    email_or_mobile_phone_field = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[3]/div/input')
    region_field = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[2]/div/div/input')
    password_confirmation_field = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/div/input')
    password_field = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/div/input')
    error_message_last_name = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')
    error_message_name = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span')
    login_button = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div/div/div[2]/button[1]')
    notification_form = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div/div')
    error_message_password = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    recover_password_button = WebElement(xpath='//*[@id="reg-err-reset-pass"]')
    close_button = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div/div/div[2]/button[2]')
    message_enter_the_phone_in_the_format = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[3]/span')
    message_must_be_filled_in_cyrillic = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')
    message_passwords_dont_match = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')


