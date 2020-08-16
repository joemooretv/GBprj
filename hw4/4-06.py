from itertools import count, cycle

# Пишем скрипт присваивания порядковых номеров по списку

# Количество порядков
loop = 3

# Список значений
obj_list = ['John', 'Martha', 'Cory', 'Kurt', 'Martin', 'Paul']

# Создаем список порядковых номеров через итератор
counter = []
for el in count(1):
    if el > loop:
        break
    else:
        counter.append(el)

# Создаем итератор полученного списка номеров
iterator = cycle(counter)

# Выводим список значений с порядковыми номерами
for el in obj_list:
    print(f'{next(iterator)}. {el}')
