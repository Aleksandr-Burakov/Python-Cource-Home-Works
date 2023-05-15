"""
Задание 4.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""
import random


class Matrix:
    def __init__(self, line_mat_1, line_mat_2):
        self.line_mat_1 = line_mat_1
        self.line_mat_2 = line_mat_2
        self.matrix = []
        for i in range(self.line_mat_1):
            self.row = []
            for j in range(self.line_mat_2):
                self.row.append(random.randint(-10, 30))
            self.matrix.append(self.row)

    def __str__(self):
        whole_matrix = ' ' '\n'
        for i in range(len(self.matrix)):
            whole_matrix = whole_matrix + '  '.join(map(str, self.matrix[i])) + '\n'
        return print(whole_matrix)

    def add_matrix(self):
        if len(obj_1.matrix) != len(obj_2.matrix) or len(obj_1.matrix[0]) != len(obj_2.matrix[0]):
            raise ValueError("Вы пытаетесь сложить матрицы разного размера!")
        whole_matrix = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(obj_1.matrix[i][j] + obj_2.matrix[i][j])
            whole_matrix.append(row)
        final_matrix = ' ' '\n'
        for i in range(len(whole_matrix)):
            final_matrix = final_matrix + '  '.join(map(str, whole_matrix[i])) + '\n'
        return final_matrix


obj_1 = Matrix(line_mat_1=int(input(f"Введите целое число, колличество строк в матрице 1: ")),
               line_mat_2=int(input(f"Введите целое число, колличество столбцов в матрице 1: ")))
obj_2 = Matrix(line_mat_1=int(input(f"Введите целое число, колличество строк в матрице 2 "
                                    f"равное колличеству строк в матрице 1: ")),
               line_mat_2=int(input(f"Введите целое число, колличество столбцов в матрице 2 "
                                    f"равное колличеству столбцов в матрице 1: ")))
print(obj_1.matrix)
print(obj_2.matrix)
print(obj_1.add_matrix())
