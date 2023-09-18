def dictionary():
    dict1 = {'name': "tom", 'age': 666}
    for key, value in dict1.items():
        print(f'key={key},value={value}')
    for key, value in enumerate(dict1, start=0):
        print(f'key={key},value={value}')


if __name__ == '__main__':
    dictionary()
