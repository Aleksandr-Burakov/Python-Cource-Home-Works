"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
import yaml

with open('file.yaml') as file:
    obj_yaml = yaml.load(file, Loader=yaml.FullLoader)
    obj_yamlw = {'items': ['computer', 'printer', 'keyboard', 'mouse'],
                 'items_price': {'computer': '400$-2000$', 'keyboard': '10$-80$',
                                 'mouse': '14$-17$', 'printer': '200$-400$'},
                 'items_quantity': 10}

with open('file.yaml', 'a', encoding='utf-8') as file:
    yaml.dump(obj_yamlw, file, indent=2, default_style=False,
              allow_unicode=True)

with open('file.yaml') as file:
    obj_yamlwr = yaml.load(file, Loader=yaml.FullLoader)

print(obj_yaml)
print(obj_yamlwr)
