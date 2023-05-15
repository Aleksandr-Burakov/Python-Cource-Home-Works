"""
Задание 2.

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:
    _mass_1 = 25
    _thickness = 0.05
    __asphalt_tonn = 1000

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        asphalt_weight = self.length * self.width * obj._mass_1 * obj._thickness
        result = asphalt_weight / obj.__asphalt_tonn
        return f"Mасса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см :\n" \
               f" {self.length}*{self.width}*{obj._mass_1}*{obj._thickness} =" \
               f" {round(asphalt_weight)} кг = {round(result)} т"


print()
obj = Road(20, 5000)
print(obj)
