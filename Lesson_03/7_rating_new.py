#  Вставляем цифру на её место в рейтинге
#  В коде особо ни чего не изменилось, просто стал обращаться к первому элементу, а вставлять весь

my_list = [[9, 'Margo'], [7, 'Bob'], [5, 'Nik'], [5, 'Nata'], [3, 'Liz']]

new_element = input("Введите новый элемент рэйтинга: ").split()
new_element[0] = int(new_element[0])

for elem in my_list:
    if new_element[0] > elem[0]:  # Если элемент больше текущего, то вставляем на его место
        my_list.insert(my_list.index(elem), new_element)
        break
    elif elem[0] == my_list[-1][0]:  # если элемент последний, то вставляем за ним
        my_list.append(new_element)
        break

print(f"Получили список: \n {my_list}")
