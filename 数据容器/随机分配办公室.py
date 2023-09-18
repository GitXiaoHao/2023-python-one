"""
8 位老师 3个办公室 将8位老师分配到3个办公室
"""
import random

teachers = ['A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H']
offices = [[], [], []]


def start():
    # 分配老师
    for name in teachers:
        ran = random.randint(0, len(offices) - 1)
        offices[ran].append(name)
    i = 1
    for (office) in offices:
        print(f"办公室{i}人数为:{len(office)},具体老师为:{office}")
        i += 1


if __name__ == '__main__':
    start()
