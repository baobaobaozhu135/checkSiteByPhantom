# _*_encoding:utf-8_*_

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities  # 预期功能 修改浏览器属性键值对
import confSetting as conf
from bs4 import BeautifulSoup
import os
from tools import get_detail_info as tool
from tools import sqlite_operation as sqlOp
import datetime
import os

#url = "http://service.spiritsoft.cn/ua.html"

def start_check(driver):
    siteInfoList = sqlOp.get_site_info()
    if siteInfoList:
        pass
    else:
        print u"没有从sqlite中取得信息，请检查"
    # print len(siteInfoList)
    # os._exit(0)
    last_url = ""  # 上一次提取的url
    print "-------------check is running----------------"
    for siteObj in siteInfoList:
        if siteObj.url != last_url:
            re_get_flag = True
        else:
            re_get_flag = False
        last_url = siteObj.url
        # print siteObj.url
        title = tool.get_title_text(driver, siteObj, re_get_flag)
        if title == "error":
            continue
        if title != siteObj.title:
            date_str = str(datetime.datetime.now())
            print u"*********发现更新************\nurl：%s\n名称：%s\n原标题：%s\n新标题：%s\n上次发现时间：%s\n此次发现时间：%s" \
                  % (siteObj.url, siteObj.url_name, siteObj.title, title,siteObj.find_date, date_str)
            # 修改数据库
            sqlOp.update_title(title, date_str, siteObj.url_id)

        else:
            print u"无更新:" + siteObj.url + "," + siteObj.title


if __name__ == '__main__':
    driver = webdriver.PhantomJS(executable_path=conf.Phantom_path,
                                 desired_capabilities=conf.set_desired_cap(),
                                 service_args=['--ignore-ssl-errors=true'])
    # 设置10秒页面超时返回，类似于requests.get()的timeout选项，driver.get()没有timeout选项
    # 以前遇到过driver.get(url)一直不返回，但也不报错的问题，这时程序会卡住，设置超时选项能解决这个问题。
    #driver.set_page_load_timeout(10)
    # 设置10秒脚本超时时间
    #driver.set_script_timeout(10)

    # phantomJS本身在多线程方面还有很多bug，建议使用多进程  TODO 待用
    #from multiprocessing import Pool
    #pool = Pool(8)
    #data_list = pool.map(get, url_list)
    #pool.close()
    #pool.join()
    start_check(driver=driver)
    # driver.close()  # 关闭当前窗口

    driver.quit()

# phantomjs timeout设置问题
# phantomjs 网页/进程关闭问题
# accept_encodiing:"identity"


