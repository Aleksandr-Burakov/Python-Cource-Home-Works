"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet
import os


def object_ping(obj):
    arguments_object = ['ping', obj]
    obj_ping = subprocess.Popen(arguments_object, stdout=subprocess.PIPE)
    print(obj_ping.stdout)
    for line_bytes in obj_ping.stdout:
        result = chardet.detect(line_bytes)
        print(line_bytes.decode(encoding=result['encoding']))
    print(os.name)


object_ping('youtube.com')
object_ping('yandex.ru')
