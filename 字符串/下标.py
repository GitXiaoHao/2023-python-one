def subscript():
    str1 = '1234'
    # 1
    print(str1[0])
    # 2
    print(str1.__getitem__(1))


def section():
    str1 = "abcdefg"
    # ace  左闭右开
    print(str1[0:5:2])
    # abcde
    print(str1[0:5:1])
    # abcde
    print(str1[0:5])
    # abcde
    print(str1[:5])
    # cdefg
    print(str1[2:])
    # abcdefg
    print(str1[:])
    # gfedcba
    print(str1[::-1])
    # cba
    print(str1[-5::-1])
    # gfedcba
    print(str1[::-1])



if __name__ == '__main__':
    section()
