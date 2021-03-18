# -*- coding:utf-8 -*-
"""
项目环境配置
"""

import os
import datetime


# 项目名称
PROJECT_NAME = 'unittest_project'

# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 各模块目录
MODULE_DIR = {
    'logs_dir': os.path.join(BASE_DIR, 'logs'),  # 日志模块目录
    'test_file_dir': os.path.join(BASE_DIR, 'test_case_file'),  # 测试用例文件目录
    'test_scripts_dir': os.path.join(BASE_DIR, 'test_scripts'),  # 测试脚本目录
    'reports_dir': os.path.join(BASE_DIR, 'reports'),  # 生成报告目录
}

# 日志文件配置
LOG_CONFIG = {
    'formatter': '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
    'console_output_level': 'DEBUG',
    'file_output_level': 'DEBUG',
    'log_file_name': os.path.join(MODULE_DIR['logs_dir'], f'{PROJECT_NAME}.log'),
    'backup_count': 5,
}

# 邮件推送配置
MAIL_CONFIG = {
    'on_off': 'off',  # 邮件推送开关：on/off
    'smtp_server': 'smtp.qq.com',  # smtp服务器（使用QQ邮箱作为服务器）
    'smtp_port': 25,  # smtp端口（使用QQ邮箱端口）
    'smtp_user': 'evan.liu@qq.com',  # smtp用户名（使用邮箱登陆账号）
    'smtp_password': '',  # smtp密码（授权码），QQ邮箱获取方式：进入QQ邮箱-设置-账户-开启服务-开启POP3/SMTP服务，然后点击生成授权码
    'sender': 'evan.liu@qq.com',  # 发件人
    'receiver': 'ziran.pipi@qq.com',  # 收件人
    'subject': '接口自动化测试报告',  # 邮件主旨
}

# 输出报告配置
OUTPUT_REPORT_CONFIG = {
    'HtmlTestRunner': {
        'report_path': os.path.join(MODULE_DIR['reports_dir'], datetime.datetime.now().strftime('%Y-%m-%d')),
        'report_name': PROJECT_NAME,
        'report_title': f'{PROJECT_NAME}_自动化测试报告',
    },
    'BeautifulReport': {
        'report_path': os.path.join(MODULE_DIR['reports_dir'], datetime.datetime.now().strftime('%Y-%m-%d')),
        'report_name': f'{datetime.datetime.now().strftime("%H_%M_%S")}_{PROJECT_NAME}',
        'report_title': f'{PROJECT_NAME}_自动化测试报告',
    },
}

# 测试启动配置
TEST_LAUNCH_CONFIG = {
    'test_scripts_path': MODULE_DIR['test_scripts_dir'],
    'execute_script_pattern': 'test_*.py',
}
