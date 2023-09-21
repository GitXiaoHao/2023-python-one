#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：2023-python-one 
@File    ：file_main.py
@IDE     ：PyCharm 
@Author  ：小豪
@Date    ：2023/9/20 21:12 
"""
import os


def file_operation():
    with open("1.txt", mode='r+') as f:
        res = f.readlines()
        f.write("6646")
        print(res)


def backups() -> None:
    """文件备份"""
    name = input("请输入备份文件:")
    # 提取后缀名
    suffix_index = name.rfind('.')
    if suffix_index <= 0:
        print("文件名无效")
        return
    # 文件名
    file_name = name[:suffix_index]
    suffix_name = name[suffix_index:]
    new_name = file_name + '[备份]' + suffix_name
    # 打开源文件
    with open(name, "rb") as old_file:
        with open(new_name, "wb") as new_file:
            while True:
                con = old_file.read(1024)
                if len(con) == 0:
                    break
                new_file.write(con)


def os_file() -> None:
    os.rename("1.txt", "2.txt")
    # I:\code\python\2023-python-one\文件 获取当前目录
    print(os.getcwd())
    # 创建文件夹
    os.mkdir("11")
    # 删除文件夹
    os.rmdir("11")
    # 改变目录路径
    os.chdir('lambda')
    # 获取目录列表
    os.listdir()
    # 文件重命名


if __name__ == '__main__':
    # backups()
    # os_file()
    pass