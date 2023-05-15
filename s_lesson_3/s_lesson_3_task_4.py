"""
4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

"""
1) используя функцию sort()
"""


def my_func(a, b):
    return a + b


first_number, second_number, third_number = int(input('Введите первое число: ')), int(input('Введите второе число: ')), \
    int(input('Введите третье число: '))
ls = list([first_number, second_number, third_number])
ls.sort(reverse=True)
first_max_number = ls[0]
second_max_number = ls[1]
result = my_func(first_max_number, second_max_number)
print(result)
"""
2) без использования функции sort()
"""


def my_func(a, b):
    return a + b


first_number, second_number, third_number = int(input('Введите первое число: ')), int(input('Введите второе число: ')), \
    int(input('Введите третье число: '))
first_sum = first_number + second_number + third_number
second_max_number = max(first_number, second_number, third_number) - min(first_number, second_number, third_number)
first_max_number = first_sum - second_max_number - min(first_number, second_number, third_number)
result = my_func(first_max_number, second_max_number)
print(result)
