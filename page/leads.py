from common.readExcel import ExcelData
from common.login import Login


class Leads(object):

    def __init__(self):
        self.a = ExcelData("快速创建潜在客户")
        self.b = Login()
        self.b.login()
        self.driver = self.b.driver  # 调用同一个driver

    def quick_c(self):  # 快速创建
        return self.driver.find_element_by_class_name(self.a.get_data('quick_creation'))

    def customer1(self):    # 潜在客户
        return self.driver.find_element_by_xpath(self.a.get_data('potential_customer1'))

    def tyc(self):  # 天眼查
        return self.driver.find_element_by_link_text(self.a.get_data('query'))

    def customer_s(self):   # 定位搜索框
        return self.driver.find_element_by_xpath(self.a.get_data('customer_search'))

    def search_b(self):     # 搜索
        return self.driver.find_element_by_xpath(self.a.get_data('search_button'))

    def choose_c(self):     # 选择搜索出来的客户
        return self.driver.find_element_by_xpath(self.a.get_data('choose_customer'))

    def lc(self):   # 选择制造流程，流程制造
        return self.driver.find_element_by_xpath(self.a.get_data('liucheng'))

    def a_people(self):     # 添加联系人
        return self.driver.find_element_by_xpath(self.a.get_data('add_people'))

    def a_name(self):   # 姓名
        return self.driver.find_element_by_xpath(self.a.get_data('add_name'))

    def a_phone(self):  # 手机
        return self.driver.find_element_by_xpath(self.a.get_data('add_phone'))

    def qd(self):   # 确定按钮
        return self.driver.find_element_by_xpath(self.a.get_data('queding'))

    def shenhe(self):   # 提交审核
        return self.driver.find_element_by_xpath(self.a.get_data('submit'))

    def c_manager(self):    # 主页面客户管理
        return self.driver.find_element_by_xpath(self.a.get_data('customer_manager'))

    def customer2(self):    # 潜在客户
        return self.driver.find_element_by_xpath(self.a.get_data('potential_customer2'))

    def get_c(self):    # 获取新建客户客户名称
        return self.driver.find_element_by_xpath(self.a.get_data('get_customer'))
