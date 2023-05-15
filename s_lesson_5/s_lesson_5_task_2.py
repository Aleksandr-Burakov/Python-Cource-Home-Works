"""
Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def digital_dok(no_ev_digit, not_even_count, even_count):
    even_digit = no_ev_digit % 10
    if no_ev_digit == 0:
        print(f" Количество нечетных чисел равно: {even_count} \n Количество четных чисел равно: {not_even_count}")
    elif even_digit % 2 == 0:
        no_ev_digit = no_ev_digit // 10
        not_even_count += 1
        return digital_dok(no_ev_digit, not_even_count, even_count)
    else:
        even_count += 1
        no_ev_digit = no_ev_digit // 10
        return digital_dok(no_ev_digit, not_even_count, even_count)


no_ev_digit = int(input(f"Введите целое число : "))
digital_dok(no_ev_digit, not_even_count=0, even_count=0)
