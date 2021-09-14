import unittest
from time import sleep
from page.customer import Customer
from common.screenShot import save_screenshot
import logging


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer()
        self.driver = self.customer.driver
        self.log = logging.getLogger()

    def tearDown(self):
        self.customer.b.login_out()

    def test_customer(self):
        self.log.info("==========快速创建目标客户==========")
        self.customer.quick_c().click()
        sleep(0.5)
        self.customer.customer1().click()
        sleep(0.5)
        self.customer.tyc().click()
        sleep(1)
        self.customer.customer_s().send_keys('语祯物联科技（上海）有限公司')
        sleep(0.5)
        self.customer.search_b().click()
        sleep(0.5)
        self.customer.choose_c().click()
        sleep(0.5)
        self.customer.jg().click()
        sleep(0.5)
        self.customer.a_people().click()
        sleep(1)
        self.customer.a_name().send_keys('李四')
        self.customer.a_phone().send_keys('13100000003')
        self.customer.qd().click()
        sleep(0.5)
        self.customer.shenhe().click()
        sleep(2)
        self.customer.c_manager().click()
        sleep(0.5)
        self.customer.customer2().click()
        sleep(6)
        customer_name = self.customer.get_c().text
        try:
            assert customer_name == u'语祯物联科技（上海）有限公司'
            self.log.info("新建目标客户为：{}".format(customer_name))
            print("快速创建目标客户测试成功...")
            self.log.info("快速创建目标客户测试成功")
        except Exception as e:
            print("快速创建目标客户测试失败！", format(e))
            save_screenshot(self.driver)
            self.log.info("快速创建目标客户测试失败")


if __name__ == "__main__":
    unittest.main()