"""Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В его
конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть
реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()),
деление (truediv()). Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
метод позволяет организовать ячейки по рядам. Метод должен возвращать строку вида *****\n*****\n*****...,
где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
ряд записываются все оставшиеся. """


class Cell:
    quantity: int

    def __init__(self, quantity: int):
        if quantity < 1:
            raise TypeError('Quantity must be more that 0')
        self.quantity = quantity

    def __add__(self, other):
        if isinstance(other, type(self)):
            return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if isinstance(other, type(self)):
            return Cell(abs(self.quantity - other.quantity))

    def __mul__(self, other):
        if isinstance(other, type(self)):
            return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        if isinstance(other, type(self)):
            return Cell(int((self.quantity + other.quantity) / 2))

    def make_order(self, row_len: int):
        res = ''
        # собираем полные ряды
        lines = self.quantity // row_len
        if lines > 0:
            for line in range(lines):
                res += '*' * lines + '\n'
        # собираем последний ряд
        last = self.quantity % row_len
        if last > 0:
            res += '*' * last
        return res


a, b = Cell(2), Cell(5)
# print((a + b).quantity)
# print((a - b).quantity)
# print((a * b).quantity)
# print((a / b).quantity)
print(b.make_order(2))
