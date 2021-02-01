#  Функция возвращает сумму двух максимальных оргументов

def max_sum(a, b, c):
    return (a + b + c)-min(a, b, c)

print(max_sum(1, 13, 2))