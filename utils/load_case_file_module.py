# -*- coding:utf-8 -*-
"""
用例文件加载模块
"""
from utils.common_module import read_excel


def read_test_data(filename):
    """
    读取用例文件的所有数据
    :param filename: 用例文件名
    :return: 返回 active 为 Y 的所有行
    {
        case_number_1: { data1, data2, data3 ... },
        case_number_2: { data1, data2, data3 ... },
        case_number_3: { data1, data2, data3 ... },
    }
    """
    data = read_excel(filename=filename)
    ready_dict = {}
    for row in data:
        temp = dict(
            case_number=row[0],
            api_host=row[2],
            request_url=row[3],
            request_method=row[4],
            request_type=row[5],
            precondition=row[6],
            request_data=row[7],
            check_point=row[8],
            active=row[9],
        )
        if temp['active'].upper() == 'Y':
            ready_dict[temp['case_number']] = temp
    return ready_dict
