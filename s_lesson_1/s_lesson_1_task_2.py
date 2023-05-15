"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
hour = 3600
minute = 60

seconds = int(input("Введите время в секундах :"))
hours = (seconds / hour) % hour
minutes = (seconds / minute) % minute
print('Время в формате чч:мм:сс -', "%02d:%02d:%02d" % (hours, minutes, seconds))
print()
onehours = round((seconds / hour), 2)
oneminutes = round((seconds / minute), 2)
print(f"Время в формате ч:м:с - {onehours}:{oneminutes}:{seconds}")
