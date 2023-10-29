'''файл с фикстурами'''

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


from data import LoginPageData
from pages.login_page import LoginPage


@pytest.fixture(autouse=True)
def browser():
    service = Service(r"/usr/local/bin/chromedriver")
    browser = webdriver.Chrome(service=service)
    browser.maximize_window()
    yield browser
    browser.quit()



@pytest.fixture()
def login(browser):
    link = LoginPageData.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    page.enter_email_valid()
    page.enter_pass()
    page.submit_btn()

