"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть.
"""
# n = input(f"Введите колличество монет лежащих на столе : ")
# back = input(f"Введите количество монет лежащих решкой вверх : ")
# front = int(n) - int(back)
# print(f"Минимальное количество монет, которые нужно перевернуть = {front}")
#
n = int(input())
count_zero = 0
count_one = 0
for i in range(n):
    x = int(input())
if x == 0:
    count_zero += 1
else:
    count_one += 1
if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)
