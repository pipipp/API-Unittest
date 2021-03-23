# -*- coding:utf-8 -*-
"""
工具模块
"""

import os
import yaml
import hashlib
import platform
import configparser
import pandas as pd

from settings import MODULE_DIR


def get_yaml_test_data(filepath):
    """
    获取yaml文件的测试数据
    :param filepath: 文件路径
    :return:
    test_data = [(http, expected), (http, expected), ...]
    """
    case = []  # 存储测试用例名称
    http = []  # 存储请求对象
    expected = []  # 存储预期结果
    with open(filepath) as f:
        data = yaml.load(f.read(), Loader=yaml.SafeLoader)
        test = data['tests']
        for each in test:
            case.append(each.get('case', ''))
            http.append(each.get('http', {}))
            expected.append(each.get('expected', {}))
    params = list(zip(case, http, expected))  # 将每条用例解包在一起
    return params


def get_excel_test_data(filename='test_api.xlsx', sheet_name=0):
    """
    读取Excel表格
    :param filename: 文件名
    :param sheet_name: 工作表名
    :return: 包含所有行的列表
    """
    filepath = os.path.join(MODULE_DIR['test_data_dir'], filename)
    if not os.path.exists(filepath):
        raise ValueError(f'({filepath}) - 文件不存在，请检查！')

    data = pd.read_excel(filepath, sheet_name=sheet_name)  # 读取表格
    data.fillna('', inplace=True)  # 替换所有的缺失值为空字符""
    new_list = data.values.tolist()
    return new_list


def get_file_md5(filepath):
    """
    获取文件内容的MD5值
    :param filepath: 文件所在路径
    :return:
    """
    with open(filepath, 'rb') as file:
        data = file.read()
    diff_check = hashlib.md5()
    diff_check.update(data)
    md5_code = diff_check.hexdigest()
    return md5_code


def read_ini_config(section, option='', filepath='config.ini', get_all=False):
    """
    读取ini配置文件
    :param section:
    :param option:
    :param filepath: 文件路径
    :param get_all: 是否获取所有的option，默认False
    :return:
    """
    config = configparser.ConfigParser()
    config.read(filepath, encoding='utf-8')  # 读取ini文件
    if get_all:
        return config.items(section)  # 返回所有的option（键值对）
    else:
        return config.get(section, option)  # 返回指定的value


def check_directory_exists(file_path):
    """
    检查文件存储路径，没有则创建
    :param file_path: 文件路径
    :return:
    """
    system_separator = '\\' if platform.system() == 'Windows' else '/'
    split_directories = file_path.split(system_separator)  # 分离所有目录名和文件名
    directories = split_directories[:-1]  # 截取所有目录名

    split_number = -1
    check_directory_list = []  # 保存所有目录的绝对路径
    for _ in range(len(directories) - 1):
        check_directory_list.append(system_separator.join(split_directories[:split_number]))
        split_number -= 1
    check_directory_list.reverse()

    # 检查每一个父目录是否存在，没有则创建
    for each_directory in check_directory_list:
        if not os.path.isdir(each_directory):
            os.mkdir(each_directory)
