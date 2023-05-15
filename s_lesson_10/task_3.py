"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""
import re


def byte_word(word_attribute, word_klass_kiril, word_def_kiril, word_typy):
    words = [word_attribute, word_klass_kiril, word_def_kiril, word_typy]
    for i in words:
        russian_words = " ".join(re.findall(r"[а-я ]+", i, re.I))
        if i != russian_words:
            result = bytes(i, 'utf-8')
            print(result)
        else:
            print(f"Слово << {i} >> - кириллица, невозможно записать в байтовом типе с помощью маркировки b'{i}'")


byte_word("attribute", "класс", "Функция", "type")
