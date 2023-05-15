"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""


def byte_word(word_class, word_function, word_method):
    words = [word_class, word_function, word_method]
    for i in words:
        result = bytes(i, 'utf-8')
        print(result)


byte_word("class", "function", "method")
