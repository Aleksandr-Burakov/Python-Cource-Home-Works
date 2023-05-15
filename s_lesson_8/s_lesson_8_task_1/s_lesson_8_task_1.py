"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.
Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;
Пример того, что должно получиться:
Изготовитель системы, Название ОС, Код продукта, Тип системы
1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based
2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based
3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based
Обязательно проверьте, что у вас получается примерно то же самое.
ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""

import re
import csv


class GetData:
    __os_prod = r'Изготовитель системы:\s*\S*'
    __os_name = r'Название ОС:\s*\S*\s*\S*\s*\S*\s*\S*\s*'
    __os_code = r'Код продукта:\s*\S*'
    __prod_reg = r'Тип системы:\s*\S*'
    __data_r = 'data_report.csv'

    def __init__(self, info):
        self.info = info
        self.__os_prod = GetData.__os_prod
        self.__os_name = GetData.__os_name
        self.__os_code = GetData.__os_code
        self.__prod_reg = GetData.__prod_reg
        self.__data_r = GetData.__data_r

    def get_os(self):
        with open(self.info, encoding='cp1251') as f_obj:
            content = f_obj.read()
            os_prod = []
            os_prod_reg = re.compile(self.__os_prod)
            os_prod.append(os_prod_reg.findall(content)[0].split()[0] + ' '
                           + os_prod_reg.findall(content)[0].split()[1])
            os_prod_reg = re.compile(self.__os_name)
            os_prod.append(os_prod_reg.findall(content)[0].split()[0] + ' '
                           + os_prod_reg.findall(content)[0].split()[1])
            os_prod_reg = re.compile(self.__os_code)
            os_prod.append(os_prod_reg.findall(content)[0].split()[0] + ' '
                           + os_prod_reg.findall(content)[0].split()[1])
            os_prod_reg = re.compile(self.__prod_reg)
            os_prod.append(os_prod_reg.findall(content)[0].split()[0] + ' '
                           + os_prod_reg.findall(content)[0].split()[1])
            result = os_prod
            return result

    def get_data(self):
        with open(self.info, encoding='cp1251') as f_obj:
            content = f_obj.read()
            os_prod_list = []
            os_prod_reg = re.compile(self.__os_prod)
            os_prod_list.append(os_prod_reg.findall(content)[0].split()[2])
            os_prod_reg = re.compile(self.__os_name)
            os_prod_list.append(os_prod_reg.findall(content)[0].split()[3] + ' '
                                + os_prod_reg.findall(content)[0].split()[4])
            os_prod_reg = re.compile(self.__os_code)
            os_prod_list.append(os_prod_reg.findall(content)[0].split()[2])
            os_prod_reg = re.compile(self.__prod_reg)
            os_prod_list.append(os_prod_reg.findall(content)[0].split()[2])
            result = os_prod_list
            return result

    def write_to(self):
        obj = list()
        obj.append(self.get_os())
        obj.append(obj_1.get_data())
        obj.append(obj_2.get_data())
        obj.append(obj_3.get_data())
        with open(self.__data_r, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(obj)
        with open(self.__data_r) as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    def __str__(self):
        return f"{self.write_to()}"


obj_1 = GetData('info_1.txt')
obj_2 = GetData('info_2.txt')
obj_3 = GetData('info_3.txt')
print(obj_1)
