from cvs import Driver
from cvs import create_driver


class CvsStoreLocator:

    def __init__(self, zipcode, driver):
        self.zipcode = zipcode
        self.driver = driver

    def locate_store(self, driver):
        driver.find_element_by_link_text('Store Locator').click()
        driver.find_element_by_id('search').send_keys('08840, NJ')
        driver.find_element_by_id('loadMore').click()
        driver.find_element_by_css_selector('label[for = "Drive_Thru"]').click()
        driver.find_element_by_id('srchstorebtn').click()
        driver.find_element_by_css_selector('a[title="08840, NJ"]').click()





def test_store_locator():
    driver = create_driver()
    url = 'https://www.cvs.com/'
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element_by_link_text('Store Locator'). click()
    driver.find_element_by_id('search').send_keys('08840, NJ')
    driver.find_element_by_id('loadMore').click()
    driver.find_element_by_css_selector('label[for = "Drive_Thru"]').click()
    driver.find_element_by_id('srchstorebtn').click()
    driver.find_element_by_css_selector('a[title="08840, NJ"]').click()
    span = driver.find_element_by_css_selector('#resultSummary > span')
    assert span.text == "08840, NJ"


locator = CvsStoreLocator()
driver = Driver()
locator.locate_store('08840, NJ')
