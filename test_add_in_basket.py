from cvs import login
from cvs import create_driver
from pytest import fail
from cvs import search
from cvs import ads_close
from cvs import find_product




def test_items_shopping_basket():
    driver = create_driver()
    login(driver)
    search(driver, 'systane ultra')
    ads_close(driver)
    product_tile = find_product(driver, 'Systane Ultra Lubricant Eye Gel Drops, Day And Night Combo Pack, 0.33oz')

    if product_tile is None:
        fail('product is not found')

    product_tile.find_element_by_class_name('cvsui-c-button').click()

