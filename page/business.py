from common.readExcel import ExcelData
from common.login import Login


class Business(object):

    def __init__(self):
        self.a = ExcelData("快速创建商机")
        self.b = Login()
        self.b.login()
        self.driver = self.b.driver  # 调用同一个driver

    def quick_creation(self):  # 快速创建
        return self.driver.find_element_by_class_name(self.a.get_data('quick_creation'))

    def business(self):
        return self.driver.find_element_by_xpath(self.a.get_data('business'))

    def add_customer(self): # 添加客户
        return self.driver.find_element_by_class_name(self.a.get_data('add_customer'))

    def customer_search(self):  # 客户搜索框
        return self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div/div/div[1]/div[4]/input')

    def search_button(self):    # 搜索按钮
        return self.driver.find_element_by_class_name(self.a.get_data('search_button'))

    def choose_customer(self):  # 选择客户
        return self.driver.find_element_by_xpath(self.a.get_data('choose_customer'))

    def ok(self):   # 确定按钮
        return self.driver.find_element_by_xpath(self.a.get_data('ok'))

    def business_name(self):    # 填写商机名称
        return self.driver.find_element_by_xpath(self.a.get_data('business_name'))

    def business_nature(self):  # 定位商机性质选择框
        return self.driver.find_element_by_xpath(self.a.get_data('business_nature'))

    def choose_nature(self):    # 选择商机性质：增购
        return self.driver.find_element_by_xpath(self.a.get_data('choose_nature'))

    def type1(self):    # 定位商机类型选择框
        return self.driver.find_element_by_xpath(self.a.get_data('type1'))

    def choose_type1(self): # 选择商机类型：分销
        return self.driver.find_element_by_xpath(self.a.get_data('choose_type1'))

    def type2(self):    # 定位分销类型选择框
        return self.driver.find_element_by_xpath(self.a.get_data('type2'))

    def choose_type2(self):     # 选择分销类型：渠道
        return self.driver.find_element_by_xpath(self.a.get_data('choose_type2'))

    def money(self):    # 预计签单金额
        return self.driver.find_element_by_xpath(self.a.get_data('money'))

    def time(self):     # 预计签单日期
        return self.driver.find_element_by_xpath(self.a.get_data('time'))

    def background(self):    # 商机背景
        return self.driver.find_element_by_xpath(self.a.get_data('background'))

    def qudaoshang(self):   # 选择渠道商
        return self.driver.find_element_by_xpath(self.a.get_data('qudaoshang'))

    def queding1(self):     # 确定渠道商
        return self.driver.find_element_by_xpath(self.a.get_data('queding1'))

    def guanlian(self):  # 关联联系人
        return self.driver.find_element_by_xpath(self.a.get_data('guanlian'))

    def choose_person(self):    # 选择联系人
        return self.driver.find_element_by_xpath(self.a.get_data('choose_person'))

    def queding2(self): # 确定联系人
        return self.driver.find_element_by_xpath(self.a.get_data('queding2'))

    def submit(self):   # 提交审核
        return self.driver.find_element_by_xpath(self.a.get_data('submit'))

    def business_manage(self):  # 商机管理
        return self.driver.find_element_by_xpath(self.a.get_data('business_manage'))

    def demand(self):   # 需求阶段
        return self.driver.find_element_by_xpath(self.a.get_data('demand'))

    def get_business(self):     # 获取新建商机商机名称
        return self.driver.find_element_by_xpath(self.a.get_data('get_business'))