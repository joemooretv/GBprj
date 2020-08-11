month = input('Go ahead: ')

# Проверка на число
if not month.isdigit():
    print('Not a number')
    exit()

# Проверка на корректность
month = int(month)
if month > 12 or month <= 0:
    print('Wrong number!')
    exit()

# Словарь

seasons_dict = {12: 'winter',
                1: 'winter',
                2: 'winter',
                3: 'spring',
                4: 'spring',
                5: 'spring',
                6: 'summer',
                7: 'summer',
                8: 'summer',
                9: 'fall',
                10: 'fall',
                11: 'fall',
                }

print(f'Dict result: {seasons_dict[month]}')

# Список

seasons_list = ['winter',
                'spring',
                'summer',
                'fall'
                ]

if month == 12 or 0 < month < 3:
    month = 0
elif 2 < month < 6:
    month = 1
elif 5 < month < 9:
    month = 2
else:
    month = 3

print(f'List result: {seasons_list[month]}')
