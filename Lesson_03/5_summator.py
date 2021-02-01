# Программа вычисляет сумму всех введённых чисел
#  выходит из суммирования по символу #, остальные символы отбрасывает

my_quit = None
my_sum = 0
print("введите числа для суммирования или !q для выхода")

while my_quit != True:  # Ждём спецсимвол для выхода
    in_list = input("введите числа или '!q': ").split()
    my_quit = True if "!q" in in_list else None  # ищем спецсимвол в строке ввода
    in_list = [int(in_l) for in_l in in_list if in_l.isdigit()]  # очищаем строку от "нечисел"
    my_sum += sum(in_list)
    print(f"Cумма равна: {my_sum}")


