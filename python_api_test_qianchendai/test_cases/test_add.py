#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : test_add.py
@Date  : 2020/4/15 0015 16:35
@Author: xibei
'''

from unittest import TestCase
from python_api_test_qianchendai.common.do_excel import DoExcel
from python_api_test_qianchendai.common.context import *
from python_api_test_qianchendai.common.do_mysql import DoMysql
from python_api_test_qianchendai.common.http_requets import HttpRequest
from python_api_test_qianchendai.common.read_conf import DoConf
from python_api_test_qianchendai.common.constant import *
import json
from ddt import data, ddt
import random
import time

sheet_name = "add"
file_name = os.path.join(test_data_dir, 'test_case.xlsx')
do_excel = DoExcel(file_name)
cases_data = do_excel.get_case(sheet_name)
conf = DoConf()


@ddt
class TestAdd(TestCase):

    @classmethod
    def setUpClass(cls):
        global mysql
        mysql = DoMysql()

    @classmethod
    def tearDownClass(cls):
        mysql.close_connect()

    def setUp(self):
        print("*" * 20 + "用例执行准备" + "*" * 20)

        # 查询配置文件中的标名是否已存在，存在：更改标名再查询
        sql = "SELECT * FROM loan WHERE Title='{}'".format(conf.get_conf_str("regex", "title"))
        mysql_result = mysql.fecth_one(sql=sql)
        # 如果存在，在标名后加入随机数，存入到Context中以用于替换
        while mysql_result:
            title_value = conf.get_conf_str("regex", "title") + "_{0}".format(random.randint(0, 1000))
            setattr(Context, 'title', title_value)
            sql = "SELECT * FROM loan WHERE Title='{}'".format(getattr(Context, 'title'))
            mysql_result = mysql.fecth_one(sql=sql)


    def tearDown(self):
        print("*" * 20 + "测试结束" + "*" * 20)

    @data(*cases_data)
    def test_add(self, case):

        # 参数检查
        url = conf.get_conf_str("api", "url") + case.url
        print("请求地址url：{}".format(url))
        params = DoRegex.replace(case.params)
        params = json.loads(params)
        print("请求参数params：{}".format(params))

        # 判断cookies是否存在Context中
        if hasattr(Context, 'cookies'):
            cookies = getattr(Context, 'cookies')
        else:
            cookies = None

        # 发起请求
        res = HttpRequest(method=case.method, url=url, params=params, cookies=cookies)

        # cookies 保存
        if res.get_cookies():
            setattr(Context, "cookies", res.get_cookies())

        # 返回结果 写入excel
        actual = res.get_text()
        do_excel.write_by_case_id(sheet_name=sheet_name, case_id=case.id, column=8, value=actual)

        # 断言期望值与返回值：状态码
        try:
            self.assertEqual(case.expect, res.get_text())
            result = 'pass'
            do_excel.write_by_case_id(sheet_name=sheet_name, case_id=case.id, column=9, value=result)
        except AssertionError as e:
            result = 'fail'
            do_excel.write_by_case_id(sheet_name=sheet_name, case_id=case.id, column=9, value=result)
            raise e

        # 查询数据库
        if case.check_sql and res.get_json()["msg"] == "加标成功":
            time.sleep(3)
            sql = "SELECT * FROM loan WHERE Title='{}'".format(params['title'])
            add_result = mysql.fecth_one(sql=sql)
            try:
                self.assertIsNotNone(add_result)
            except AssertionError as e:
                print("数据库未查询到该标")
                raise e



