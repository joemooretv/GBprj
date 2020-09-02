"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде. Далее реализовать перегрузку
метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица. """


class Matrix:

    def __init__(self, data: list):
        self.column_len = len(data[0])
        self.row_len = len(data)
        for row in data:
            # проверка на длину
            if len(row) != self.column_len or len(row) < 1:
                raise TypeError('Incorrect row length')
            # проверка на тип
            for el in row:
                if type(el) != int and type(el) != float:
                    raise TypeError(f'Wrong element type {type(el)}')
        self._data = data

    def __str__(self):
        # формируем финальную строку
        result_str = 'Your matrix:\n'
        for row in self._data:
            line = str(row).strip('[]') + '\n'
            result_str += line
        return result_str

    def __add__(self, other):
        # проверка на класс второго элемента
        if not isinstance(other, Matrix):
            raise TypeError('At least one of objects is not instance of Matrix')
        # проверка на равное количество строк
        if self.row_len != other.row_len:
            raise ValueError('Stroke\'s quantity isn\'t equal')
        # проверка на равное количество столбцов
        if self.column_len != other.column_len:
            raise ValueError('Stroke\'s quantity isn\'t equal')
        # сборка новой матрицы
        res = []
        for row in range(self.row_len):
            x = self._data[row]
            y = other._data[row]
            new_row = [x[column] + y[column] for column in range(self.column_len)]
            res.append(new_row)
        return Matrix(res)


a = Matrix([[4, 6, 7], [5, 7, 6]])
b = Matrix([[3, 2, 22], [1, -2, 6]])
print(a + b)
