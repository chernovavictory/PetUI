from locators.login_page_locators import LoginPageLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage
from data import LoginPageData

'''Клик - это сразу клик. Сабмит когда кнопка закрыта'''


class LoginPage(BasePage):

    def enter_email(self, email):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(email)

    def enter_email_valid(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(LoginPageData.LOGIN_EMAIL)

    def enter_pass(self):
        login_pass = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_pass.send_keys(LoginPageData.LOGIN_PASS)

    def submit_btn(self):
        login_btn = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_btn.submit()

    # def find_profile(self):
    #     profile = self.browser.find_element(*ProfilePageLocators.ADD_PET_BUTTON)
    #     return profile
        '''return обязателен, так как просто ищем элемент'''






