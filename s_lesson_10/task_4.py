"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""


def byte_word(word_development, word_administration, word_protocol, word_standard):
    words = [word_development, word_administration, word_protocol, word_standard]
    count = 1
    for i in words:
        result = str.encode(i, encoding='utf-8')
        print(f"\n{count}) {result}")
        print(f"{count})", type(result))
        result_2 = bytes.decode(result, encoding='utf-8')
        print(f"{count}) {result_2}")
        print(f"{count})", type(result_2), "\n")
        count += 1


byte_word("разработка", "администрирование", "protocol", "standard")
