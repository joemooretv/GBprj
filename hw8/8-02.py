"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой. """


class MyZeroDiv(Exception):

    def __str__(self):
        return 'You trying to division on zero'


try:
    x = int(input('Insert first number: '))
    y = int(input('Insert second number: '))
    if y == 0:
        raise MyZeroDiv
    print(x / y)
except ValueError:
    print('Use numbers only')
except MyZeroDiv:
    print('You trying to division on zero')
