"""
Задание 1.

Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.

Пример:
Ведите ваше имя: Василий
Ведите ваш пароль: vas
Введите ваш возраст: 45
Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45
"""

print()
surname = 'Иванов'
firstname = 'Василий'
city = 'Пыть-Ях'
print("{} {}, город: {}.".format(firstname, surname, city))
print()

"""Пользователь вводит свое имя с новой строки"""

print("Введите Ваше имя :")
name = input()

"""Используя строку кода приведенную ниже,
   пользователь будет вводит свое имя в этой же строке"""
# name = input("Введите Ваше имя :")

print("Введите Ваш пароль :")
password = input()

"""Используя строку кода приведенную ниже,
   пользователь будет вводит свой пароль в этой же строке"""
# password = input("Введите Ваш пароль :")

"""Пользователь вводит свой возраст в этой же строке"""
age = input("Введите Ваш возраст :")
print()
print(f"Ваши данные для входа в аккаунт : имя - {name}, пароль - {password}, возраст - {age} ;")
