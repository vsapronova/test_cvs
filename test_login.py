import pytest
from selenium import webdriver
from cvs import login
from cvs import create_driver


@pytest.fixture(scope='module')
def driver_logged_in():
    driver = create_driver()
    login(driver)
    yield driver
    print("teardown driver")
    driver.close()



def test_login(driver_logged_in):
    sign_out = driver_logged_in.find_element_by_class_name("sign-out")
    assert "Sign Out" in sign_out.text


def test_account_email(driver_logged_in):
    driver_logged_in.find_element_by_link_text("My Account").click()
    email = driver_logged_in.find_element_by_css_selector("span.text-info")
    assert email.text == "v.sapronova@gmail.com"


def test_header3(driver_logged_in):
    driver_logged_in.find_element_by_tag_name('h3')

def test_pharmacy(driver_logged_in):
    driver_logged_in.find_element_by_link_text('Pharmacy')


def test_clinic(driver_logged_in):
    driver_logged_in.find_element_by_link_text('MinuteClinic')


def test_shop(driver_logged_in):
    driver_logged_in.find_element_by_link_text('Shop')


def test_search_box(driver_logged_in):
    driver_logged_in.find_element_by_id('searchbox')


def test_items_shopping_basket(driver_logged_in):
    driver_logged_in.find_element_by_class_name('head-basket')





