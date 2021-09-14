# coding:utf-8
import time
import os
from common.report import report_out
from common.log import log_out
from common.sendEmail import send_email


def report_address(reports_address):
    # 测试报告文件夹中所有的文件加入到列表
    test_report_list = os.listdir(reports_address)
    # 按照升序排序生成新的列表
    new_test_report_list = sorted(test_report_list)
    # 获取最新的测试报告
    the_last_report = new_test_report_list[-1]
    # 最新的测试报告地址
    the_last_report_address = os.path.join(reports_address, the_last_report)
    return the_last_report_address


def run_case():
    print("============开始运行============")
    curpath = os.path.dirname(os.path.realpath(__file__))
    report_dir = os.path.join(curpath, "report/")  # 测试报告存放目录
    log_dir = os.path.join(curpath, 'log/')  # 日志存放目录
    test_dir = os.path.join(curpath, "testcase/")  # 测试用例读取目录
    name_project = "DOM"
    log_out(log_dir, name_project)
    report_out(test_dir, report_dir, name_project)
    time.sleep(5)
    send_email(report_address(report_dir), mail_to=['2686086371@qq.com'])
    print("============执行结束============")


if __name__ == '__main__':
    run_case()
