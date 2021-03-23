# -*- coding:utf-8 -*-
"""
装饰器模块
"""

import os
import datetime
import functools

from utils.loggers import LOGGER


# 测试参数打印装饰器
def test_param_print():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__  # 获取测试函数名
            LOGGER.debug(f'开始执行用例：{func_name}')

            LOGGER.debug('测试数据' + '*' * 50)
            for each in args[1:]:  # 打印所有测试数据
                LOGGER.debug(each)
            LOGGER.debug('*' * 58)

            start_time = datetime.datetime.now()
            LOGGER.debug(f'执行时间：{start_time}')

            try:
                func(*args, **kwargs)  # 执行测试函数
            except Exception as ex:
                LOGGER.error(f'执行失败，错误信息：{ex}')

            end_time = datetime.datetime.now()
            LOGGER.debug(f'结束时间：{start_time}，耗时：{(end_time - start_time).total_seconds()}s')
        return wrapper
    return decorator
