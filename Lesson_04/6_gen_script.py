#  Программа скрипт для генерации последовательностей.
# совмещу оба скрипта в одном за счёт ключей

# Примеры коммандных строк
# 6_gen_script.py --start_gen 10
# 6_gen_script.py --list er df cv rt fg vb
# 6_gen_script.py -h
# 6_gen_script.py --list er df cv rt fg vb --start_gen 10

from argparse import ArgumentParser
import random

parser = ArgumentParser()

# Описываем аргумент для старта последовательности
parser.add_argument(
    '--start_gen',
    type=int,
    default=None,
    help='генерирует список из 10 целых чисел начиная с заданного')

# Описываем аргумент для списка генерации последовательности
parser.add_argument('--list',
                    type=str,
                    default=None,
                    nargs='+',
                    help='генерирует последовательность из 10 элементов введённого списка')

args = parser.parse_args()  # передаём полученные параметы


def gen_int(start_gen):
    print([el for el in range(start_gen, start_gen + 11)])


def gen_list(in_list):
    print([random.choice(in_list) for _ in range(10)])


gen_int(args.start_gen) if args.start_gen is not None else None
gen_list(args.list) if args.list is not None else None
