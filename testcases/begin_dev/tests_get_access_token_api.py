#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: tests_get_access_token_api.py
# @time: 2021/3/14 2:27 下午

import unittest
import requests
import jsonpath
from common.log_utils import logger
from common.config_utils import config
from common import public_api_infos

class TestsGetAccessTokenApi(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = config.HOSTS
        self.session = requests.session()
    def tearDown(self) -> None:
        self.session.close()

    def test_01_get_access_token(self):
        logger.info('***********************************')
        logger.info('*     用例【VXC_KS_001】开始执行     *' )
        try:
            url_params = {
                "grant_type":"client_credential",
                "appid":"wx55614004f367f8ca",
                "secret":"65515b46dd758dfdb09420bb7db2c67f"
            }
            response = public_api_infos.get_access_token_api(self.session,url_params)
            json_body = response.json()
            actual_result = jsonpath.jsonpath(json_body,'$.access_token')[0]
            self.assertTrue( actual_result )
        except AssertionError as e:
            logger.info('*     用例【VXC_KS_001】断言失败     *')
        except Exception as e:
            logger.error('%s'%e.__str__())
        finally:
            logger.info('*      用例【VXC_KS_001】执行结束    *')
            logger.info('***********************************')


    def test_02_grant_type_none(self):
        self._testMethodName = 'VXC_KS_002'
        self._testMethodDoc = '验证grant_type不填值时，获取access_token接口能否正常处理'
        url_params = {
            "grant_type":"",
            "appid":"wx55614004f367f8ca",
            "secret":"65515b46dd758dfdb09420bb7db2c67f"
        }
        response = public_api_infos.get_access_token_api(self.session,url_params)
        json_body = response.json()
        actual_result = jsonpath.jsonpath(json_body,'$.errcode')[0]
        self.assertEqual( actual_result , 40002 )

if __name__=='__main__':
    unittest.main(verbosity=2)