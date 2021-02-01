#  Task: написать свой генератор для считывания файлов один раз

import os

my_path = os.getcwd()


# print(path)
# files = os.listdir(path)
# print(files)

def file_list(my_path):
    for my_file in os.listdir(my_path):
        yield my_file


for my_file in file_list(my_path):
    print(my_file)

# Task попробовать заменить на лямбда функцию my_f

from functools import reduce

# def my_f(symbol_1, symbol_2):
#     return symbol_1 + symbol_2
#
# random_str = ['a', 'b', 'c', 'b', 'd']
# print(reduce(my_f, random_str))

random_str = ['a', 'b', 'c', 'b', 'd']
print(reduce(lambda a, b: a + b, random_str))  # Заменил


# Task попробовать сделать рекурсивный вызов

def my_f(my_list):
    if len(my_list) == 1:
        return my_list
    else:
        my_list[0] = ''.join(my_list[0] + my_list[1])
        my_list.pop(1)
        my_f(my_list)
    return str(my_list[0])


print(my_f(random_str))
