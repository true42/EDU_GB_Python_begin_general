#  программа убирает из списка повторяющиеся элементы в списке

import random
len_list = 30  # длинна списка, чем больше, тем больше вероятность повторения
max_list_mean = 50  # максимальное значение элемента. чем меньше тем больше повторений

# Функция генерации списка случайных чисел заданной длинны
def gen_list(len_list):
    return [random.randint(1, max_list_mean) for _ in range(len_list)]

new_list = gen_list(len_list)
print(f'исходный список: \n{new_list}')

# чистим список от повторяющихся значений
print([el for el in new_list if new_list.count(el) == 1])