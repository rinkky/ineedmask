import time

def order(driver, market='jd'):
    try:
        if market == 'jd':
            return order_jd(driver)
    except:
        return False

def order_jd(driver):
    add_cart = driver.find_element_by_id('InitCartUrl')
    add_cart.click()
    time.sleep(0.1)
    driver.get('https://cart.jd.com/cart.action')
    submit_btn = driver.find_element_by_class('submit-btn')
    submit_btn.click()
    time.sleep(0.2)
    driver.find_element_by_id('order-submit').click()
    return True
