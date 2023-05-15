"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

*Попытайтесь получить кодовые точки без онлайн-конвертера!
без хардкода!

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""


def parsing_words(word_1, word_2, word_3):
    words_string = [word_1, word_2, word_3]
    for i in words_string:
        word_list = []
        for j in i:
            word_list.append(j)
        word_str = ''.join(map(str, word_list))
        print(f"'{word_str}'")
        for k in word_str:
            word_li = []
            for j in k:
                word_li.append(j)
                words = str.encode(j, encoding='unicode_escape')
                word_unicode = words.decode('utf-8')
                print(f"{word_unicode}", end='')
        print()


parsing_words('разработка', 'сокет', 'декоратор')
