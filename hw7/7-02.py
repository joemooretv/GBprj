"""Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 +
0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property. """

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, title, measure, size):
        self.title = title
        self.measure = measure
        self.size = size

    @property
    def title(self):
        return self._title

    @property
    def measure(self):
        return self._measure

    @property
    def size(self):
        return self._size

    @title.setter
    def title(self, title):
        self._title = title

    @measure.setter
    def measure(self, measure):
        self._measure = measure

    @size.setter
    def size(self, size):
        self._size = size

    @abstractmethod
    def tissue_quantity(self):
        pass


class Coat(Clothes):
    def tissue_quantity(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def tissue_quantity(self):
        return round(self.size * 2 + 0.3, 2)


coat = Coat('Pal\'to', 'numbering', 4)
print(f'{coat.title} size: {coat.size} ({coat.measure}). Tissue rate: {coat.tissue_quantity()}')

suit = Suit('Kostyum', 'rost cm', 163)
print(f'{suit.title} size: {suit.size} ({suit.measure}). Tissue rate: {suit.tissue_quantity()}')
