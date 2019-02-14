
from cvs import login
from cvs import create_driver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_items_shopping_basket():
    driver = create_driver()
    login(driver)
    driver.find_element_by_class_name('head-basket').click()
    driver.find_element_by_css_selector('h1.cart__header')
    wait = WebDriverWait(driver, 10)
    wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'cart__header')))
    item = driver.find_element_by_class_name('item__name-heading')
    assert item.text == 'Flexitol Heel Balm, 3 OZ'

    select = Select(driver.find_element_by_class_name('item__quantity-dropdown'))
    select.select_by_value('5')
    

