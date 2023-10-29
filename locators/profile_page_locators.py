from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_PET_IMG = (By.CSS_SELECTOR, 'div:nth-child(1) > div > img')
    ADD_PET_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/div[1]/div/div[1]/button')
    ADD_PET_NAME = (By.ID, 'name')
    CHOOSE_PET_TYPE = (By.CSS_SELECTOR, '#typeSelector')
    CHOOSE_PET_TYPE_CAT = (By.XPATH, '//*[@aria-label="cat"]')
    CHOOSE_PET_GENDER = (By.CSS_SELECTOR, '#genderSelector')
    CHOOSE_PET_GENDER_MALE = (By.XPATH, '//*[@aria-label="Male"]')
    ADD_PET_AGE = (By.CSS_SELECTOR, '#age > input')
    SUBMIT_ADD_PET_BTN = (By.XPATH, '//*[@aria-label="Submit"]')
    CHOOSE_PHOTO_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div[2]/div/span/input')
    SUBMIT_PHOTO_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div[2]/div')
    PET_CARD = (By.CLASS_NAME, 'col-12')

