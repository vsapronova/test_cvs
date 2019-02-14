from selenium import webdriver
import time


def test_search_box():
    driver = webdriver.Chrome('/Users/victoria/Downloads/chromedriver')
    url = 'https://www.cvs.com/'
    driver.get(url)
    driver.find_element_by_id('searchbox')
    print('searchbox')
