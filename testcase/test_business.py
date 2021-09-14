import unittest
from time import sleep
from page.business import Business
from common.screenShot import save_screenshot
import logging

class TestBusiness(unittest.TestCase):

    def setUp(self):
        self.business = Business()
        self.driver = self.business.driver
        self.log = logging.getLogger()

    def tearDown(self):
        self.business.b.login_out()

    def test_business(self):
        self.log.info("==========快速创建商机==========")
        self.business.quick_creation().click()
        sleep(0.5)
        self.business.business().click()
        sleep(0.5)
        self.business.add_customer().click()
        sleep(0.5)
        self.business.customer_search().send_keys('青岛')
        sleep(0.5)
        self.business.search_button().click()
        sleep(0.5)
        self.business.choose_customer().click()
        sleep(0.5)
        self.business.ok().click()
        sleep(0.5)
        self.business.business_name().clear()
        self.business.business_name().send_keys('测试商机名称')
        sleep(0.5)
        self.business.business_nature().click()
        sleep(0.5)
        self.business.choose_nature().click()
        sleep(0.5)
        self.business.type1().click()
        self.business.choose_type1().click()
        sleep(0.5)
        self.business.type2().click()
        self.business.choose_type2().click()
        sleep(0.5)
        self.business.money().send_keys('1000')
        sleep(0.5)
        self.business.time().send_keys('2021-11-11')
        sleep(0.5)
        self.business.background().send_keys('商机背景填充')
        sleep(0.5)
        self.business.qudaoshang().send_keys('青岛利信通数控设备有限公司')
        sleep(2)
        self.business.queding1().click()
        sleep(0.5)
        self.business.guanlian().click()
        sleep(1)
        self.business.choose_person().click()
        sleep(0.5)
        self.business.queding2().click()
        sleep(0.5)
        self.business.submit().click()
        sleep(2)
        self.business.business_manage().click()
        sleep(0.5)
        self.business.demand().click()
        sleep(5)
        business_name = self.business.get_business().text
        try:
            assert business_name == u'测试商机名称'
            self.log.info("新建商机为：{}".format(business_name))
            print("快速创建商机测试成功...")
            self.log.info("快速创建商机测试成功")
        except Exception as e:
            print("快速创建商机测试失败！", format(e))
            save_screenshot(self.driver)
            self.log.info("快速创建商机测试失败！")


if __name__ == "__main__":
    unittest.main()