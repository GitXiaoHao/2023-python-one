#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：2023-python-one
@File    ：学员管理系统.py
@IDE     ：PyCharm
@Author  ：小豪
@Date    ：2023/9/20 14:36
"""
id_str = "id"
name_str = "name"
tel_str = 'tel'


def info_print():
    """
    定义功能界面函数
    :return:
    """
    print('请选择功能----------')
    print('1. 添加')
    print('2. 删除')
    print('3. 修改')
    print('4. 查找')
    print('5. 显示所有')
    print('6. 退出')


def add_info():
    """
    添加
    :return:
    """
    global info
    new_id = input("请输入学号：")
    new_name = input("请输入姓名：")
    new_tel = input('请输入手机号：')
    for i in info:
        if new_id == i[id_str]:
            print("学号不能重复")
            return
    info_dict = {
        id_str:   new_id,
        name_str: new_name,
        tel_str:  new_tel
    }
    info.append(info_dict)


def remove_info():
    global info
    del_id = input("请输入要删除学员的姓名：")
    # 判断是否存在
    for i in info:
        if del_id == i[id_str]:
            info.remove(i)
            print("删除成功")
            break
    else:
        print("不存在，删除失败！")


def modify_info():
    pass

def start(num):
    if num.isnumeric():
        num = int(num)
    else:
        print("输入错误，请重新输入")
        return
    if num == 1:
        add_info()
    elif num == 2:
        remove_info()
    elif num == 3:
        modify_info()
    elif num == 4:
        pass
    elif num == 5:
        pass
    print(info)


info = []
if __name__ == '__main__':
    user_num = 1
    while user_num != "6":
        info_print()
        user_num = input("请输入功能序号：")
        start(user_num)
