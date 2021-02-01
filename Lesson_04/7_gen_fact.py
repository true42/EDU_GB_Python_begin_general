#  Программа генерирует факториалы чисел до n

from functools import reduce

i = 1

def my_fact(n):
    for i in range(2, n+2):
        yield (reduce(lambda a, b: a * b, [el for el in range(1, i)]))


for el in my_fact(10):
    print(f'{i}! = {el}')
    i += 1
