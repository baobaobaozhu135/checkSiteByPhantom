# _*_encoding:utf-8_*_

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities  # 预期功能 修改浏览器属性键值对
from main import confSetting as conf
from bs4 import BeautifulSoup
import os
import traceback
from selenium.common.exceptions import NoSuchElementException

def get_title_text(driver, siteInfo, re_get=False):  # 是否需要重新加载，默认是否
    if re_get:
        #print len(driver.window_handles)
        if len(driver.window_handles) > 1:
            driver.close()  # 保持只有一个页面进程
        #print driver.current_window_handle
        driver.get(siteInfo.url)
        # print siteInfo.css_selector
    try:
        #print siteInfo.css_selector
        titleObj = driver.find_elements_by_css_selector(siteInfo.css_selector)
        title_text = ""
        if titleObj:
            for title in titleObj:
                title_text = title_text + title.text
        else:
            title_text = "error"
    except NoSuchElementException:
        traceback.print_exc()

    return title_text
