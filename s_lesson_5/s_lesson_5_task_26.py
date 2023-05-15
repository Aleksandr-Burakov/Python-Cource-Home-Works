"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
 и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""


def Exponentiation_numbers(number_a, number_b):
    if number_b == 1:
        return number_a
    elif number_b % 2 == 0:
        result = Exponentiation_numbers(number_a, number_b // 2)
        return result * result
    else:
        result = Exponentiation_numbers(number_a, number_b // 2)
        return result * result * number_a


number_a, number_b = int(input(f"Введите целое число a: ")), int(input(f"Введите целое число b: "))
print(Exponentiation_numbers(number_a, number_b))
