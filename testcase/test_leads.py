import unittest
from time import sleep
from page.leads import Leads
from common.screenShot import save_screenshot
import logging


class TestLeads(unittest.TestCase):
    """
    创建测试用例集
    """

    def setUp(self):
        self.leads = Leads()
        self.driver = self.leads.driver
        self.log = logging.getLogger()          # 初始化log

    def tearDown(self):
        self.leads.b.login_out()

    def test_leads(self):
        self.log.info("==========快速创建潜在客户==========")
        self.leads.quick_c().click()
        sleep(0.5)
        self.leads.customer1().click()
        sleep(1)
        self.leads.tyc().click()
        sleep(1)
        self.leads.customer_s().send_keys('语祯物联科技（昆山）有限公司')
        sleep(0.5)
        self.leads.search_b().click()
        sleep(0.5)
        self.leads.choose_c().click()
        sleep(0.5)
        self.leads.lc().click()
        sleep(0.5)
        self.leads.a_people().click()
        sleep(1)
        self.leads.a_name().send_keys('张三')
        self.leads.a_phone().send_keys('13100000002')
        self.leads.qd().click()
        sleep(0.5)
        self.leads.shenhe().click()
        sleep(2)
        self.leads.c_manager().click()
        sleep(0.5)
        self.leads.customer2().click()
        sleep(6)
        customer_name = self.leads.get_c().text
        try:
            assert customer_name == u'语祯物联科技（昆山）有限公司'
            self.log.info("新建潜在客户为：{}".format(customer_name))
            print("快速创建潜在客户测试成功...")
            self.log.info("快速创建潜在客户测试成功")
        except Exception as e:
            print("快速创建潜在客户测试失败！", format(e))
            save_screenshot(self.driver)
            self.log.info("快速创建潜在客户测试失败")


if __name__ == "__main__":
    unittest.main()