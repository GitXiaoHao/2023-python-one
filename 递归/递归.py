#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：2023-python-one 
@File    ：递归.py
@IDE     ：PyCharm 
@Author  ：小豪
@Date    ：2023/9/20 18:57 
"""


def sum_number(num):
    if num == 1:
        return 1
    return num + sum_number(num - 1)


if __name__ == '__main__':
    print(sum_number(3))
    print((lambda a, b: a + b)(1, 2))
