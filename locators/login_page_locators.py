from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    # LOGIN_EMAIL = (By.XPATH, '//*[@id="login"]')
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    # LOGIN_PASS = (By.XPATH, '//*[@id="password"]/input')
    # LOGIN_BTN = (By.CLASS_NAME, "p-button-label")
    LOGIN_BTN = (By.XPATH, '//*[@id="pv_id_2_content"]//button')
    PROFILE = (By.XPATH, '//*[@id="app"]/header/div/ul/li[1]/a')


