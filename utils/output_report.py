# -*- coding:utf-8 -*-
"""
输出报告模块
"""

import HtmlTestRunner

from BeautifulReport import BeautifulReport
from settings import OUTPUT_REPORT_CONFIG


def run_and_generate_test_report_from_htr(suite):
    """
    运行测试集，并使用 HtmlTestRunner 模块生成测试报告
    :param suite: 测试集
    :return: 生成报告路径，list
    """
    config = OUTPUT_REPORT_CONFIG['HtmlTestRunner']
    runner = HtmlTestRunner.HTMLTestRunner(output=config['report_path'],
                                           report_name=config['report_name'],
                                           report_title=config['report_title'])
    result = runner.run(suite)
    report_path = result.report_files
    return report_path


def run_and_generate_test_report_from_br(suite):
    """
    运行测试集，并使用 BeautifulReport 模块生成测试报告
    :param suite: 测试集
    :return: 生成报告路径，list
    """
    config = OUTPUT_REPORT_CONFIG['BeautifulReport']
    report_path = BeautifulReport(suite).report(description=config['report_title'],
                                                filename=config['report_name'], report_dir=config['report_path'])
    return [report_path]
