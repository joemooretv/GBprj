res = float(input('Укажите дистанцию (км) первой тренировки: '))
stop = float(input('Какого результата вы хотите достичь? '))
day = 1

while True:
    if res >= stop:
        break
    day += 1
    res = res * 1.1

print('На {:d}-й день ваш результат будет не менее {:.1f} км.'.format(day, stop))
