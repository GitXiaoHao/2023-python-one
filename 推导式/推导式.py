# 创建一个列表 创建一个0-10的列表
def list_derivation():
    # 1.
    list1 = []
    for i in range(0, 11):
        list1.append(i)
    print(list1)
    # 2. 列表推导式
    list1 = [i for i in range(11)]
    print(list1)
    # 3. 带 if 偶数
    list2 = [i for i in range(20) if i % 2 == 0]
    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    print(list2)
    # 4. 多个for循环实现列表推导式
    list3 = [(i, j) for i in range(3) for j in range(3)]
    # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    print(list3)


def dictionary_derivation():
    dist1 = {i: i ** 2 for i in range(5)}
    # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    print(dist1)
    # 合并两个列表合并为一个字典
    list1 = ['name', 'age', 'gender']
    list2 = ['Tom', 20, 'man']
    dist2 = {list1[i]: list2[i] for i in range(min(len(list1), len(list2)))}
    # dist2 = {list1[i]: list2[i] for i in range(len(list1))}
    # {'name': 'Tom', 'age': 20, 'gender': 'man'}
    print(dist2)
    # 提取目标数据
    counts = {"MBP": 268, "HP": 125, "DELL": 201, "Lenovo": 199, "acer": 99}
    count1 = {k: v for (k, v) in counts.items() if v >= 200}
    # {'MBP': 268, 'DELL': 201}
    print(count1)


def set_derivation():
    list1 = [1, 2, 5]
    set1 = {i ** 2 for i in list1}
    # {1, 4, 25}
    print(set1)


if __name__ == '__main__':
    # list_derivation()
    # dictionary_derivation()
    set_derivation()
