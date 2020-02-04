import time

from alert import alert
from selenium import webdriver
from config.logger import logger
from config import get_all_products
from .driverctl import get_driver
from .order import order

def check(driver, url, no_keyword='无货', yes_keyword='有货', out_keyword='下柜', name=None):
    driver.get(url)
    page_source = driver.page_source
    desc = '{} {}'.format(url, name)
    if no_keyword in page_source:
        logger.info('{} check result: sold out'.format(desc))
        return False
    elif out_keyword in page_source:
        logger.info('{} check result: 下架'.format(desc))
        return False
    elif yes_keyword in page_source:
        logger.info('{} check result: in sell'.format(desc))
        alert('{} in sell'.format(desc))
        return True
    logger.warning('{} check result: unkown error'.format(desc))
    return False

def check_all(driver=None, do_order=False):
    need_driver = not driver
    if need_driver:
        driver = get_driver()
    products = get_all_products()

    for product in products:
        name = product.get('name', '')
        url = product['url']
        desc = '{} {}'.format(url, name)
        if check(driver, product['url'], name=name) and do_order:
            if order(driver):
                msg = '{} 已尝试提交订单，请尽快查看并付款'.format(desc)
                logger.info(msg)
                alert(msg)
            else:
                logger.error('{} 提交订单失败'.format(desc))            
        time.sleep(0.5)
    if need_driver:
        driver.close()

def check_forever():
    logger.info('check begin...')
    driver = get_driver(headless=False)
    login(driver)
    try:
        while True:
            check_all(driver)
            time.sleep(10)
    except Exception as err:
        logger.info(err)
        driver.close()
    logger.info('check end.')

def login(driver):
    while True:
        driver.get('https://passport.jd.com/new/login.aspx')
        input('请手动登录，然后在这里输入回车')
        if check_login(driver):
            return True
        print('未检测到登录状态，请重试')

def check_login(driver):
    driver.get('https://www.jd.com/')
    if '请登录' in driver.page_source:
        return False
    return True
