# -*- coding:utf-8 -*-
"""
测试启动程序
"""
# @Author : 孜然v
# @Python : 3.7.4

import unittest

from utils.email_push import MAIL_PUSH
from settings import TEST_LAUNCH_CONFIG, MAIL_CONFIG
from utils.output_report import run_and_generate_test_report_from_br


class TestLaunch(object):

    def __init__(self, test_scripts_path, execute_script_pattern='test_*.py'):
        """
        测试启动配置
        :param test_scripts_path: 测试脚本所在目录
        :param execute_script_pattern: 定义需要启动哪些测试脚本
        """
        self.test_scripts_path = test_scripts_path
        self.execute_script_pattern = execute_script_pattern
        self.report_generate_path = None

    def run_test_case(self):
        """执行测试用例，并生成测试报告"""
        discover = unittest.defaultTestLoader.discover(start_dir=self.test_scripts_path,
                                                       pattern=self.execute_script_pattern)
        self.report_generate_path = run_and_generate_test_report_from_br(suite=discover)

    def mail_push(self):
        """将生成的测试报告推送到邮箱"""
        if MAIL_CONFIG['on_off'] == 'on':
            with open(self.report_generate_path[0], 'r', encoding='utf-8') as rf:
                MAIL_PUSH.send_mail(sender=MAIL_CONFIG['sender'], receiver=MAIL_CONFIG['receiver'],
                                    subject=MAIL_CONFIG['subject'],
                                    body=rf.read(), attachments=self.report_generate_path)

    def main(self):
        self.run_test_case()
        self.mail_push()


if __name__ == '__main__':
    test_launch = TestLaunch(TEST_LAUNCH_CONFIG['test_scripts_path'], TEST_LAUNCH_CONFIG['execute_script_pattern'])
    test_launch.main()
