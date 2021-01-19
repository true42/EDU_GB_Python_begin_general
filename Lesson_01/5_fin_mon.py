# Программа по финансовому мониторингу предприятия

revenue = int(input("Введите сумму выручки: "))
costs = int(input("Введите сумму издержек: "))
# revenue = 456
# costs = 123
if revenue > costs:
    profit = revenue - costs
    print(f"Прибыль предприятия составлиа: {profit}")
    print(f"Рентабельность выручки составила: {profit / revenue * 100:.02f}%")
    employees = int(input("Введите количество штатных сотрудников: "))
    print(f"Прибыль фирмы в рассчёте на одного сотрудника составляет: {profit / employees:.02f}")
else:
    print(f"К сожалению фирма сейчас находится в убытке {revenue - costs}")

