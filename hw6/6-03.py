"""Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров). """


class Worker:
    name: str
    surname: str
    position: str
    __income: {}

    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name, self.surname, self.position, self.__income = name, surname, position, income

    def get_income(self, param):
        return self.__income.get(param)


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        try:
            return self.get_income('wage') + self.get_income('bonus')
        except TypeError:
            return 'wrong param'


worker = Position('John', 'Doe', 'Supervisor', {'wage': 10000, 'bonus': 505})
print(f'Worker: {worker.get_full_name()}, Total salary: {worker.get_total_income()}')
