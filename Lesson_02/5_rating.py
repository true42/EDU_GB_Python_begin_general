#  Вставляем цифру на её место в рейтинге

my_list = [9, 7, 5, 5, 3]

new_element = int(input("Введите новый элемент рэйтинга: "))
# Решение не верное, т.к. не вставит значение не из списка, точнее вставит его в конец

# if new_element in my_list:
#     my_list.insert(my_list.index(new_element)+my_list.count(new_element), new_element)
# elif new_element > max(my_list):
#     my_list.insert(0, new_element)
# else:
#     my_list.insert(len(my_list), new_element)

# Ршение рабочее, но мне что-то не нравится, не красивое какое-то.
# Если будет время попробую написать красиво
for elem in my_list:
    if new_element > elem:  #  Если элемент больше текущего, то вставляем на его место
        my_list.insert(my_list.index(elem), new_element)
        break
    elif elem == my_list[-1]:  # если элемент последний, то вставляем за ним
        my_list.append(new_element)
        break

print(f"Получили список: \n {my_list}")

# Попробую в одну строку, но это будет нечитаемо...
# my_list.insert(0, new_element) if new_element > max(my_list) else my_list.insert(len(my_list), new_element)
# print([my_list.insert(my_list.index(elem), new_element) for elem in my_list if new_element > elem])
