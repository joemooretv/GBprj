"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат. """

import time


class Car:
    speed: int  # ускорение в секундах до 100км/ч
    color: str
    name: str
    is_police: bool
    __time: float = 0

    def __init__(self, color, speed, name='My_Car', is_police=False):
        self.color, self.speed, self.name, self.is_police = \
            color, 100 / speed, name, is_police

    def go(self):
        # Записываем время старта в приватную переменную
        self.__time = time.time()
        print(f'{self.name} start driving')
        return 0

    def stop(self):
        # Обнуляем время
        self.__time = 0
        print(f'{self.name} stopped')

    def turn(self, direction):
        print(f'{self.name} turned {direction}')

    def show_speed(self):
        if self.__time != 0:
            cur_seconds = time.time() - self.__time
        else:
            cur_seconds = 0
        # Выводим скорость при равноускоренном движении
        cur_speed = round(self.speed * cur_seconds)
        print(f'Current {self.name} speed: {cur_speed} km/h')
        return cur_speed


class TownCar(Car):

    def __init__(self, color, speed=11.6, name='My_TownCar'):
        super().__init__(color, speed, name, False)

    def show_speed(self):
        cur_speed = super(TownCar, self).show_speed()
        if cur_speed >= 60:
            print('Slow down, cowboy!')


class WorkCar(Car):

    def __init__(self, color, speed=13.2, name='My_WorkCar'):
        super().__init__(color, speed, name, False)

    def show_speed(self):
        cur_speed = super(WorkCar, self).show_speed()
        if cur_speed >= 40:
            print('Slow down, cowboy!')


class SportCar(Car):

    def __init__(self, color, speed=6.1, name='My_SportCar'):
        super().__init__(color, speed, name, False)


class PoliceCar(Car):

    def __init__(self, speed=8.7, name='My_PoliceCar'):
        super().__init__('White/Blue', speed, name, True)


# Ниже примеры
my_car = WorkCar('green', 7.9)
print(my_car)
print(my_car.is_police)
my_car.show_speed()
my_car.go()
time.sleep(2)
my_car.show_speed()
my_car.turn('right')
time.sleep(2)
my_car.show_speed()
my_car.stop()
my_car.show_speed()

my_car = PoliceCar()
print(f'Try next: \n{my_car.color} {my_car.name}')
