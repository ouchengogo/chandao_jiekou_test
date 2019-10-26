# conding: utf-8
from bs4 import BeautifulSoup
import re
import requests
import time
import unittest
import warnings#未写忽略警告函数时，执行结果处会提示“ResourceWarning: unclosed <socket.socket fd=288, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 3411), raddr=('127.0.0.1', 8090)>”
"""登录禅道主界面，过程涉及Apache用户zentao,密码123456;操作人员账号：zhangcheng,密码：1q2w3e4r5t"""
host_value = "http://127.0.0.1:8090/"

class login_test(unittest.TestCase):
    #报文头
    u"测试登录禅道，包括用户名、密码的正常值、异常值场景！"
    headers = {"Authorization":"Basic emVudGFvOjEyMzQ1Ng==",
               "Accept-Encoding":"gzip, deflate, br",
               "Accept-Language":"zh-CN, zh;q = 0.9"
               }
    #用户列表
    user = ("zhangcheng","zhangsan","zhangcheng")
    #密码列表
    password = ("000000","1q2w3e4r5t","1q2w3e4r5t")
    count = 0
    @classmethod
    def setUpClass(cls):
        u"前提条件"
        warnings.simplefilter("ignore", ResourceWarning)#忽略警告，不让其在执行结果中显示
        cls.se = requests.session()
        response_r1 = cls.se.get(host_value + "index.php", headers=login_test.headers)#输入zentao;123456的接口
        time.sleep(2)
        response_r2 = cls.se.get(host_value + "pro/api-getLicenses.html", headers = login_test.headers)#选择开源版的接口，此时会获取到一个set_cookies"zentaoid"
        time.sleep(2)
    # 登录用户名和密码为正常值
    def testcase_001(self):
        u"登录密码错误！"
        data_value = {"passwordStrength": "1"}
        data_value["account"] = login_test.user[0]
        data_value["password"] = login_test.password[0]
        response_r3 = login_test.se.post(host_value + "zentao/user-login-L3plbnRhby8=.html", headers=login_test.headers, data=data_value)
        self.assertEqual(200, response_r3.status_code)
        self.assertIn("登录失败，请检查您的用户名或密码是否填写正确", response_r3.text)
    # 登录用户名错误
    def testcase_002(self):
        u"登录用户名错误！"
        data_value = {"passwordStrength": "1"}
        data_value["account"] = login_test.user[1]
        data_value["password"] = login_test.password[1]
        response_r4 = login_test.se.post(host_value + "zentao/user-login-L3plbnRhby8=.html", headers=login_test.headers, data=data_value)
        self.assertEqual(200, response_r4.status_code)
        self.assertIn("登录失败，请检查您的用户名或密码是否填写正确", response_r4.text)
        time.sleep(2)
    # 密码错误
    def testcase_003(self):
        u"登录用户名和密码正确！"
        data_value = {"passwordStrength": "1"}
        data_value["account"] = login_test.user[2]
        data_value["password"] = login_test.password[2]
        response_r5 = self.se.post(host_value + "zentao/user-login-L3plbnRhby8=.html", headers=login_test.headers, data=data_value)
        response_r5_text = re.findall("location='(.+?)'", response_r5.text)
        self.assertEqual(200, response_r5.status_code)
        self.assertEqual(response_r5_text[0], "/zentao/index.html")
        self.assertTrue(response_r5_text[0])
        time.sleep(2)
    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == "__main__":
    unittest.main()