# _*_encoding:utf-8_*_

from elems.site_info import siteInfo
import sqlite3
from main import confSetting as conf
import datetime
import traceback


def get_site_info():
    conn = None
    cursor = None
    try:
        conn = sqlite3.connect(conf.sqlite_path)
        cursor = conn.cursor()
        sql = "select * from site_info"
        cursor.execute(sql)
        values = cursor.fetchall()
        siteObjList = []
        if values:
            for value in values:
                site_info = siteInfo()
                site_info.url_id = value[0]
                site_info.url_item = value[1]
                site_info.url = value[2]
                site_info.url_name = value[3]
                site_info.css_selector = value[4]
                site_info.title = value[5]
                site_info.find_date = value[7]
                siteObjList.append(site_info)
    except Exception as e:
        print str(e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return siteObjList
'''
siteObjList = get_site_info()
if siteObjList:
    for obj in siteObjList:
        print obj.url_item + obj.url_name + obj.url + obj.title
'''


# 更改数据库标题和时间
def update_title(title, date_str, url_id):
    conn = None
    cursor = None
    try:
        #print "title" + title
        #print "date_str:" + date_str
        conn = sqlite3.connect(conf.sqlite_path)
        cursor = conn.cursor()
        # sql = "update site_info set title = '" + title + "', find_date = '" + date_str + "'"
        sql = "update site_info set title = '%s', find_date = '%s' where url_id = %s" %(title, date_str, url_id)
        # print sql
        cursor.execute(sql)

    except Exception as e:
        print traceback.print_exc()
    else:
        conn.commit()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


