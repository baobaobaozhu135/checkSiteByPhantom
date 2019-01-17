# _*_encoding:utf-8_*_
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


Phantom_path = r"C:\Program Files (x86)\phantomjs-2.1.1-windows\bin\Phantomjs.exe"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134 "
accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"  # 请求头accept


headers = {
    "User-Agent": user_agent,
    "Accept": accept
}

timeout = 5

# 设置desired_capabilities的PhantomJS属性，修改请求头
def set_desired_cap():
    dcap = dict(DesiredCapabilities.PHANTOMJS)  # 转化为字典（本来就是键值对）
    # dcap["User-Agent"] = conf.use_agent  # 不好用
    dcap['phantomjs.page.settings.userAgent'] = user_agent
    # dcap["Accept"] = conf.accept
    dcap['phantomjs.page.settings.accept'] = accept
    dcap['phantomjs.page.settings.resourceTimeout'] = timeout
    return dcap

# sqlite path
sqlite_path = "../resource/mysitedb.db"


