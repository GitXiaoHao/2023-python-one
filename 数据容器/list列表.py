def list_demo():
    name_list = ['list', True, 666]
    # ['list', True, 666]
    # <class 'list'>
    print(name_list)
    print(type(name_list))
    # 嵌套的列表
    name_list = [['yu', 666, True], [True, False]]
    """
    [['yu', 666, True], [True, False]]
    <class 'list'>
    """
    print(name_list)
    print(type(name_list))


# 列表下标索引
def subscript_index():
    name_list = ['list', True, 666]
    # 正向索引 list
    print(name_list[0])
    # 反向索引 666 True
    print(name_list[-1], name_list[-2])
    # 嵌套下标索引
    name_list = [['yu', 666, True], [True, False]]
    # True True
    print(name_list[-1][0], name_list[-2][-1])



# 列表常用操作
def common_operations():
    pass


if __name__ == '__main__':
    # subscript_index()
    common_operations()