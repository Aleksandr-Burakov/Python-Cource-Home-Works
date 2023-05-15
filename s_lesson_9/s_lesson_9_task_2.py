"""
Задание 2. реализовать метакласс. позволяющий создавать всегда один и тот же объект класса

"""


class TypedMeta(type):
    __a = None

    def __call__(cls, *args, **kwargs):
        if cls.__a is None:
            cls.__a = super.__call__(*args, **kwargs)
        return cls.__a


class MyClass(metaclass=TypedMeta):

    def method_1(self):
        pass

    def method_2(self):
        print("Небольшая проблема")


obj_1 = MyClass()
obj_2 = MyClass()
obj_3 = MyClass()
print(obj_1 is obj_3)
print(obj_1)
print(obj_2)
print(obj_3)
