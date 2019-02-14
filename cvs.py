from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


def login(driver):
    url = 'https://www.cvs.com/'
    driver.get(url)
    head = driver.find_element_by_class_name("head-c1-right")
    head.find_element_by_id("signInBtn").click()
    form = driver.find_element_by_class_name("signin-body")
    email = form.find_element_by_id("clubLoginEmail")
    email.clear()
    email.send_keys("v.sapronova@gmail.com")
    password = form.find_element_by_id("clubLoginPwd")
    password.clear()
    password.send_keys("mamapapa11!")
    driver.find_element_by_css_selector('.signin-button > button').click()
    wait = WebDriverWait(driver, 10)
    wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'sign-out')))


def search(driver, product):
    search_box = driver.find_element_by_id('searchbox')
    search_box.send_keys(product)
    search_box.send_keys(Keys.ENTER)

    wait = WebDriverWait(driver, 10)
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'h1.gbcvs-c-pageHd__heading')))



def ads_close(driver):
    try:
        close_ads_button = driver.find_element_by_css_selector('a.acsCloseButton.acsAbandonButton')
        close_ads_button.click()
    except NoSuchElementException:
        pass


def find_product(driver, product):
    tiles = driver.find_elements_by_tag_name('gb-product')
    for tile in tiles:
        product_link = tile.find_element_by_css_selector('a.gbcvs-c-productTile__link')
        print(product_link.text)
        if product_link.text == product:
            return tile
    return None


def create_driver():
    driver = webdriver.Chrome('/Users/victoria/Downloads/chromedriver')
    driver.implicitly_wait(10)
    return driver