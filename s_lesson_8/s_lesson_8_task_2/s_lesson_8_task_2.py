"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": []
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять,
а потом сохранять все в файл
"""

import json


def write_order_to_json(item, quantity, price, buyer, data):
    with open('orders.json') as file:
        obj = json.load(file)
        obj['orders'].append({'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'data': data})
    with open('orders.json', 'w') as file:
        json.dump(obj, file, indent=4)


write_order_to_json('tv samsung', '30', '40000', 'Egorov L.E', '11.01.2022')