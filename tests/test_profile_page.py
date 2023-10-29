
import time
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common import TimeoutException

from data import ProfilePageData, LoginPageData
from locators.profile_page_locators import ProfilePageLocators
from pages.profile_page import ProfilePage



def test_add_pet(browser, login):
    link = ProfilePageData.PROFILE_PAGE_URL
    page = ProfilePage(browser, link)
    wait = WebDriverWait(browser, timeout=1)
    page.open()
    page.go_to_add_pet_button()
    page.go_to_add_pet_name()
    page.go_to_add_pet_age()
    page.go_to_choose_pet_type()
    page.choose_pet_type_cat()
    page.go_to_choose_pet_gender()
    page.choose_pet_gender_male()
    page.submit_add_pet_btn()
    wait.until(page.element_is_visible(ProfilePageLocators.CHOOSE_PHOTO_BTN, 3))
    page.send_pet_photo()
    # wait.until(page.element_is_visible(ProfilePageLocators.SUBMIT_PHOTO_BTN, 3))
    page.submit_add_pet_photo()
    # wait.until(page.url_to_be(ProfilePageData.PROFILE_PAGE_URL, 5))

    assert page.text_to_be_present_in_element(ProfilePageLocators.PET_CARD, ProfilePageData.VALID_PET_NAME)
