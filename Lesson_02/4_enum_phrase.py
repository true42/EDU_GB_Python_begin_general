#  Разбиваем строку на слова и нумеруем их

sentence = 'Это_тестовое предложение для проверки работы программы c очень_длинным_словом.'

# sentence = input("Введите строку слов разделённую пробелами")
print(sentence, "\n")

word_list = sentence.split()

for ind, el in enumerate(word_list):
    print(f'{ind} {el[:10]}')

# пробую сделать в одну строку
print("\n та же операция в одну строку:")
print(*[" ".join([str(ind), el[:10]]) for ind, el in enumerate(word_list)], sep='\n')
