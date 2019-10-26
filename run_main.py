# coding:utf-8
from common.HTMLTestRunner import HTMLTestRunner
import os
import time
import unittest



#获取测试用例的路径
realpath_run_main = os.path.realpath(__file__)#获取当前文件的路径全称
dirpath_run_main = os.path.dirname(realpath_run_main)#获取当前文件所处路径
filename_of_save_testcase = "testcase"#存储测试用例的文件名称
testcase_dirname = os.path.join(dirpath_run_main, filename_of_save_testcase)#存储测试用例的路径

#获取测试报告的路径,增加个时间戳
localTime = time.localtime(time.time())
timestamp = time.strftime('%Y_%m_%d_%H_%M_%S', localTime)

report_file = "testreport" + str(timestamp) + ".html"#创建一个名称为testreport的测试报告
filename_of_save_report = "report"#存储测试报告的文件名称
report_dirname = os.path.join(dirpath_run_main, filename_of_save_report)#获取测试报告的绝对路径，连续两次join，第一次join
report_realname = os.path.join(report_dirname, report_file)#获取测试报告的绝对路径，连续两次join，第二次join。两次join也可以写到一起，一次join实现

#创建report
open_file = open(report_realname, "wb")
discover = unittest.defaultTestLoader.discover(testcase_dirname, pattern="test*.py")#在存储测试用例路径下寻找名称为test开头的.py文件；
runner = HTMLTestRunner(open_file, title="禅道登录接口测试报告", description="测试结果如下：")
runner.run(discover)#运行测试用例集
open_file.close()
# runner = unittest.TextTestRunner()#创建运行器，另一个运行器这个是基于unittest库