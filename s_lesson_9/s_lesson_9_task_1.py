"""

Задание 1. Реализовать дескрипторы для любых двух классов

"""


class NonNegative:

    def __set__(self, instance, value):
        if type(value) is str:
            raise ValueError("Значение не может быть строкой")
        instance.__dict__[self.my_attr] = value
        if value < 0:
            raise ValueError("Значение не может отрицательным")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class NonString:

    def __set__(self, instance, value):
        if type(value) is int:
            raise ValueError("Значение не может быть числом")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    hours = NonNegative()
    payment = NonNegative()
    name = NonString()
    surname = NonString()

    def __init__(self, name, surname, hours, payment):
        self.name = name
        self.surname = surname
        self.hours = hours
        self.payment = payment

    def total_profit(self):
        return self.hours * self.payment


obj = Worker('Иван', 'Иванов', 200, 30)
print(f" Сотрудник компании : \n {obj.name} {obj.surname}")
print(f" Заработная плата : {obj.total_profit()} у.е")
