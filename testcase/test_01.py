# conding: utf-8
from bs4 import BeautifulSoup
import re
import requests
import time
import unittest
import warnings#未写忽略警告函数时，执行结果处会提示“ResourceWarning: unclosed <socket.socket fd=288, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 3411), raddr=('127.0.0.1', 8090)>”
"""登录禅道主界面，过程涉及Apache用户zentao,密码123456;操作人员账号：zhangcheng,密码：1q2w3e4r5t"""

class login_test(unittest.TestCase):
    #报文头
    headers = {"Authorization":"Basic emVudGFvOjEyMzQ1Ng==",
               "Accept-Encoding":"gzip, deflate, br",
               "Accept-Language":"zh-CN, zh;q = 0.9"
               }
    #用户列表
    user = ("zhangcheng","zhangsan","zhangcheng")
    #密码列表
    password = ("1q2w3e4r5t","1q2w3e4r5t","000000")
    count = 0
    def setUp(self):
        u"前提条件，执行多次！"
        warnings.simplefilter("ignore", ResourceWarning)#忽略警告，不让其在执行结果中显示
        self.se = requests.session()
        response_r1 = self.se.get("http://127.0.0.1:8090/index.php", headers=login_test.headers)#输入zentao;123456的接口
        time.sleep(2)
        response_r2 = self.se.get("http://127.0.0.1:8090/pro/api-getLicenses.html", headers = login_test.headers)#选择开源版的接口，此时会获取到一个set_cookies"zentaoid"
        self.data_value = {"passwordStrength": "1"}
        self.data_value["account"] = login_test.user[login_test.count]
        self.data_value["password"] = login_test.password[login_test.count]
        login_test.count = login_test.count + 1
        time.sleep(2)
    # 登录用户名和密码为正常值
    def testcase_001(self):
        u"登录用户名、密码为正常值-多次前置版!"
        response_r3 = self.se.post("http://127.0.0.1:8090/zentao/user-login-L3plbnRhby8=.html", headers=login_test.headers, data=self.data_value)
        response_r3_text = re.findall("location='(.+?)'", response_r3.text)
        self.assertEqual(200,response_r3.status_code)
        self.assertEqual(response_r3_text[0], "/zentao/index.html")
        self.assertTrue(response_r3_text[0])
    # 登录用户名错误
    def testcase_002(self):
        u"登录用户名错误-多次前置版!"
        response_r4 = self.se.post("http://127.0.0.1:8090/zentao/user-login-L3plbnRhby8=.html", headers=login_test.headers, data=self.data_value)
        self.assertEqual(200, response_r4.status_code)
        self.assertIn("登录失败，请检查您的用户名或密码是否填写正确", response_r4.text)
    # 密码错误
    def testcase_003(self):
        u"登录密码错误-多次前置版!"
        response_r5 = self.se.post("http://127.0.0.1:8090/zentao/user-login-L3plbnRhby8=.html", headers=login_test.headers, data=self.data_value)
        self.assertEqual(200, response_r5.status_code)
        self.assertIn("登录失败，请检查您的用户名或密码是否填写正确", response_r5.text)
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()