#  программа генерирует список и выбирает элементы которые боьлше предыдущего аргумента в этом же списке.

import random

new_list = 30
count_list = 0


# Функция генерации списка случайных чисел заданной длинны
def gen_list(len_list):
    return [random.randint(1, 100) for _ in range(len_list)]


# функция выбора элементов списка, которые больше предыдущего
def cut_list(new_list):
    return [new_list[el + 1] for el in range(len(new_list) - 1) if new_list[el] < new_list[el + 1]]


# Генерируем новый список заданной длинны
new_list = gen_list(new_list)  # Да, я знаю, что преобразую типы и в С++ так никогда бы не сделал, но...

print(f'исходный список: \n{new_list} длинной {len(new_list)}')

# а теперь режем списки пока не останется один или ноль аргументов, да, такое тоже бывает!
while len(new_list) > 1:
    new_list = cut_list(new_list)
    count_list += 1
    print(f'итерация №{count_list}. Список {new_list} длинной {len(new_list)}')
