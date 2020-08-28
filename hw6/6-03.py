"""Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров). """


class Worker:
    name: str
    surname: int
    position: str
    __income: {}

    def __init__(self, name: str, surname, position, income):
        self.name, self.surname, self.position, self.__income = name, surname, position, income


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self.__income('wage') + self.__income('bonus')


a = Worker('John', 'Doe', 'Supervisor', 1236)
print(a.surname)

b = Worker
print(b)

c = Position('Dohn', 'Toe', 'Hypervisor', 1236)
print(c.get_full_name())
