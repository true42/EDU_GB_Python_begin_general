#    функция деления числа

def divide(a, b):
    return a / b if b != 0 else None

print(f'Результат деления = {divide(int(input("введите делимое: ")), int(input("введите делитель: ")))}')