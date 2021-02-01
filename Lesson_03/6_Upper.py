#  Программа делает первую букву заглавной

def my_upper(word):  # функция переводит в заглавные первую букву слова
    return word.title()

def my_upper_ord(word):  # функция делает заглавную букву через код символа
    return chr(ord(word[0]) - 32) + word[1:]

print(my_upper(input('введите слово: ')))

my_list = input("Введите строку из слов: ")

print(' '.join(list(map(my_upper, my_list.split()))))  # вызываем my_upper для каждого слова и выводим в одной строке

# можно дойти до одной строки вообще, но мне кажется она будет уже плохо читаться
# print(' '.join(list(map(my_upper, my_list.split(input("Введите строку из слов: "))))))

# Развлекаться так по полной!
print(' '.join(list(map(my_upper_ord(), my_list.split(input("Введите строку из слов: "))))))
