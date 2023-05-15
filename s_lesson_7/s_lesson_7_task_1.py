"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time


class TrafficLight:

    def __init__(self, color_red, color_yellow, color_green):
        self.__color_red = color_red
        self.__color_yellow = color_yellow
        self.__color_green = color_green

    def running(self):
        print(f"\033[0;30;41m {self.__color_red} \033[0;0m")
        time.sleep(7)
        print(f"\033[0;30;43m {self.__color_yellow} \033[0;0m")
        time.sleep(2)
        print(f"\033[0;30;42m {self.__color_green} \033[0;0m")
        time.sleep(3)


obj = TrafficLight(' red  ', 'yellow', 'green ')
obj.running()
