"""
2. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).
Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!
Process finished with exit code 0
Пример:
Введите первое число: 10
Введите второе число: 10
1.0
Process finished with exit code 0
"""


def fission_result(first_number, second_number):
    try:
        print(f"Результат деления: {round((first_number / second_number), 2)}")
    except (ZeroDivisionError, ValueError):
        print("Попытка деления числа на ноль или некорректный ввод")
        print("Завершение программы")


first_num, second_num = int(input("Введите первое число: ")), int(input("Введите второе число: "))
fission_result(first_num, second_num)
