earn = float(input('Укажите выручку за расчетный период: '))
outlay = float(input('Укажите издержки за расчетный период: '))
odd = earn - outlay

if 0 < odd:
    profit = odd / earn * 100
    staff = int(input('Ваша прибыль составила {:.1f} \n'
                      'Рентабельность в текущем периоде {:.1f}% \n'
                      'Укажите количество сотрудников: '.format(odd, profit)))
    print('Прибыль в расчете на одного сотрудника составляет {:.1f}'.format(odd / staff))
elif odd == 0:
    print('Вы вышли в ноль')
else:
    print('Вы потеряли {:.1f}'.format(-odd))
