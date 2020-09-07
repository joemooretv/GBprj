class MyZeroDiv(Exception):

    def __str__(self):
        return 'You trying to division on zero'


x = int(input('Insert first number: '))
y = int(input('Insert second number: '))
if y == 0:
    raise MyZeroDiv

try:
    print(x / y)
except MyZeroDiv as exp:
    print('You tried to division on zero')
