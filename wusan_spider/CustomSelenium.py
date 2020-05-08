# -*- coding: utf-8 -*-
# ==========================================
# Author : mk
# Create Time : 2020/5/7 - 10:46
# File Name : CustomSelenium.py
# Description : 
# Software: PyCharm
# ==========================================
from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options


class BrowserDriver:
    def __init__(self, engine='Chrome'):
        if engine == 'Firefox':
            self.browser = webdriver.Firefox()
        elif engine == 'Chrome':
            options = Options()
            options.add_argument("--headless")
            self.browser = webdriver.Chrome(chrome_options=options)

    def open(self, url):
        self.browser.get(url)

    def close(self):
        self.browser.close()


if __name__ == "__main__":
    driver = BrowserDriver()
    driver.open("http://zy.quyixian.com/NewFiveThreeB/")
    # layer1 class = g-margin-x-lgr
    data_years = driver.browser.find_elements_by_class_name('g-margin-x-lgr')
    for d in data_years:
        print(d.text)
    # layer2 class = gl-flex-grow js-filter-choose
    # gm-filter-choose g-margin-y-sm gl-flex
    labels = driver.browser.find_elements_by_tag_name('a')
    try:
        for l in labels:
            if l.get_attribute('class') == 'down gl-flex gl-flex-cross-center js-down':
                driver.browser.execute_script("arguments[0].click();", l)
                # l.click()
                # time.sleep(1)
                # driver.browser.back()
                print(l.text)
    except Exception as e:
        print(e)
    # driver.close()
