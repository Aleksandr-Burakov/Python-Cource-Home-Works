"""
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""
import random

min_number = int(input(f"Введите число от 0 до 20, начало диапазона: "))
max_number = int(input(f"Введите число от 0 до 20, конец диапазона: "))
ell_list = [random.randint(-10, 30) for _ in range(20)]
print(*[el for el in range(len(ell_list)) if min_number <= ell_list[el] <= max_number])
print(ell_list)
