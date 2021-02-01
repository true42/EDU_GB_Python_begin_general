#  программа рассчитывает зарплату
# Необходимо запускать как скрипт с параметрами. Пример коммандной строки представлен ниже

# from sys import argv

# python3 1_Script.py --name Ive --howo 160.5 --hoco 355.5 --priz 30000
from argparse import ArgumentParser  # подключаем модуль, чтоб красиво работать с аргументами

parser = ArgumentParser()  # наследуем класс для работы с параметрами

parser.add_argument('--name', type=str)
parser.add_argument('--howo', type=float)
parser.add_argument('--hoco', type=float)
parser.add_argument('--priz', type=int)

args = parser.parse_args()  # передаём полученные параметы

print(f'зарплата для {args.name} составит {args.howo * args.hoco + args.priz} руб.')
