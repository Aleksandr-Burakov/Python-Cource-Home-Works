"""
Задание 3. Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
"""


#
# Реверс любых символов в строке при помощи рекурсии и срезов.
#
# def rev_nu(in_nu):
#     if len(in_nu) == 1:
#         return in_nu
#     return in_nu[-1] + rev_nu(in_nu[:-1])
#
#
# in_nu = input(f"Введите любые символы: ")
# print(rev_nu(in_nu))
#

def rev_nu(in_nu, nu):
    if in_nu == 0:
        print(nu[1:])
    else:
        dig = in_nu % 10
        in_nu = in_nu // 10
        nu = str(nu) + str(dig)
        return rev_nu(in_nu, nu)


in_nu = int(input(f"Введите целое число a: "))
rev_nu(in_nu, nu=0)