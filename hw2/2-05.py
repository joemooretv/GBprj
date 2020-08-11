chart = [7, 5, 3, 3, 2]

while True:
    print(f'\nРейтинг: {chart}\n'
          f'Для выхода введи \'q\'\n')
    new_el = input('Введите новый результат: ')

    # Выходим из программы
    if new_el == 'q':
        exit()

    # Проверка на число
    if not new_el.isdigit():
        print('Допустимы только положительные числа')
        continue

    new_el = int(new_el)

    # Если число меньше последнего
    if chart[-1] >= new_el:
        chart.append(new_el)
        continue

    # Если число больше одного из элементов
    for el in chart:
        if new_el > el:
            chart.insert(chart.index(el), new_el)
            break
