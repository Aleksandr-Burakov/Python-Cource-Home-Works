"""
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
*Пример:*
2 2
    4
"""


def numbers_sum(number_a, number_b):
    print(number_a, number_b)
    if number_b == 0:
        return number_a
    return numbers_sum(number_a + 1, number_b - 1)


number_a, number_b = int(input(f"Введите целое число a: ")), int(input(f"Введите целое число b: "))
print(f" Сумма двух целых неотрицательных чисел:  {numbers_sum(number_a, number_b)}")
