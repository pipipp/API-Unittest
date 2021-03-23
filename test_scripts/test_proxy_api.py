import os
import unittest
import requests

from ddt import ddt, data, unpack
from utils.tools import get_yaml_test_data
from utils.loggers import LOGGER
from utils.directors import test_param_print
from settings import MODULE_DIR


# 获取测试数据
test_data = get_yaml_test_data(os.path.join(MODULE_DIR['test_data_dir'], 'proxy.yaml'))


@ddt
class TestAPI(unittest.TestCase):

    def setUp(self):
        """在每个测试方法之前执行"""
        pass

    def tearDown(self):
        """在每个测试方法之后执行"""
        pass

    @test_param_print()
    @unpack
    @data(*test_data)
    def test_proxy(self, case, http, expected):
        r = requests.request(http['method'],
                             url=http['host'] + http['path'],
                             headers=http['headers'],
                             params=http['params'])
        resp = r.json()

        self.assertEqual(resp['status'], expected['response']['status'])
        self.assertEqual(resp['message'], expected['response']['message'])
        self.assertEqual(bool(resp['data']), expected['response']['data'])
