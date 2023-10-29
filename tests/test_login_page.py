import time
import pytest
import allure
from allure_commons.types import AttachmentType

from selenium.common import TimeoutException

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


from data import LoginPageData
from locators.login_page_locators import LoginPageLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.login_page import LoginPage





@allure.feature('user_login')
@allure.story('Inter the valid email data for logging in')
@allure.severity('blocker')
def test_login(browser):
    link = LoginPageData.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    wait = WebDriverWait(browser, 10)
    page.open()
    allure.step('Вводим email')
    page.enter_email(LoginPageData.LOGIN_EMAIL)
    wait.until(EC.presence_of_element_located(LoginPageLocators.LOGIN_BTN))
    allure.step('Вводим password')
    page.enter_pass()
    allure.step('Нажимаем кнопку submit')
    page.submit_btn()
    check = page.presence_of_element_located(ProfilePageLocators.ADD_PET_BUTTON)
    with allure.step('Делаем скриншот'):
        allure.attach(browser.get_screenshot_as_png(), name='result_login', attachment_type=AttachmentType.PNG)
    assert check



@allure.feature('user_login')
@allure.story('Inter the invalid email data for logging in')
@allure.severity('blocker')
def test_login_invalid(browser):
    link = LoginPageData.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    allure.step('Вводим email')
    page.enter_email(LoginPageData.LOGIN_EMAIL_INVALID)
    allure.step('Вводим password')
    page.enter_pass()
    allure.step('Нажимаем кнопку submit')
    page.submit_btn()
    check = page.presence_of_element_located(LoginPageLocators.LOGIN_EMAIL)
    with allure.step('Делаем скриншот'):
        allure.attach(browser.get_screenshot_as_png(), name='result_login', attachment_type=AttachmentType.PNG)
    assert check










