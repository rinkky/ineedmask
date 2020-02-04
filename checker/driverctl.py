import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver(headless=True):
    options = Options()
    if headless:
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
    # user_data_dir = os.path.join(os.path.dirname(__file__), os.path.pardir, 'user_data')
    # user_data_dir = os.path.realpath(user_data_dir)
    # options.add_argument('--user-data-dir={}'.format(user_data_dir))
    options.add_argument('--disable-extensions')
    options.add_argument('log-level=2')

    # if nopic:
    #     prefs = {'profile.managed_default_content_settings.images': 2}
    #     options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(chrome_options=options)
    driver.implicitly_wait(5)
    return driver
