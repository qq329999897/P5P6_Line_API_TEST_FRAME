#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: tests_create_user_tag_api.py
# @time: 2021/3/14 3:17 下午

import unittest
import requests
import json
import jsonpath
from common.config_utils import config
from common import public_api_infos

class TestsCreateUserTagApi(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = config.HOSTS
        self.session = requests.session()
    def tearDown(self) -> None:
        self.session.close()

    def test_01_create_user_tag(self):
        self._testMethodName = 'VXC_YH_002'
        self._testMethodDoc = '验证调用创建标签接口，标签名参数与已存在的标签重名能否正常处理'
        token_id = public_api_infos.get_access_token(self.session)
        url_params = {
            "access_token":token_id
        }
        post_data_json = {  "tag" : {     "name" : "湖南长沙"   } }
        response = public_api_infos.create_user_tag_api(self.session,url_params,post_data_json)

        actual_result = jsonpath.jsonpath( response.json(),'$.errcode' )[0]
        self.assertEqual( actual_result,45157 )

if __name__=='__main__':
    unittest.main(verbosity=2)