# _*_encoding:utf-8*_


class siteInfo(object):
    # 对应sqlite信息
    def __init__(self):
        self.url_id = ""  # id
        self.url_item = ""  # 项目名
        self.url = ""  # url地址
        self.url_name = ""  # url名称
        self.css_selector = "" # css选择器
        self.title = ""  # 原标题
        self.release_date = ""  # 发布时间
        # self.new_title = ""  # 新标题
        # self.new_release_date = ""  # 新发布时间
        self.find_date = ""  # 发现时间
        self.need_phantom = 0  # 是否需要phantom浏览器进行访问