#  Возведение числа в степень

def my_pow(x, y):  # Простая функция степени
    return x ** y


# самостоятельный подсчёт
def my_pow_2(x, y):
    out = 1
    if y < 0:  # если степень отрицательная
        for i in range(abs(y)):  # считаем знаменатель
            out *= x
        return 1 / out  # вычислаяем степень
    else:
        for i in range(y):  # если степень положительная
            out *= x
        return out


x = 2
y = -3
print(my_pow(x, y))
print(my_pow_2(x, y))
