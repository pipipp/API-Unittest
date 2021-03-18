import unittest

from test_scripts.case_top import CaseTop
from utils.load_case_file_module import read_test_data


TEST_DATA = read_test_data('test_api.xlsx')  # 读取用例文件数据


class TestAPI(CaseTop):
    """
    执行用例，需要手动添加测试脚本
    """

    @unittest.skipUnless(TEST_DATA.get('proxy_001'), 'Skip')
    def test_proxy_001(self):
        self.start_case(**TEST_DATA['proxy_001'])

    @unittest.skipUnless(TEST_DATA.get('proxy_002'), 'Skip')
    def test_proxy_002(self):
        self.start_case(**TEST_DATA['proxy_002'])
