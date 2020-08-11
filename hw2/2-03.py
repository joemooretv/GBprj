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

# Заводим список множеств значений для месяцев
seasons_ids = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

# Заводим список времен года
seasons_list = ['winter',
                'spring',
                'summer',
                'fall'
                ]

# Создаем пустой словарь
seasons_dict = {}

# Проходим по каждому множеству месяцев
for key, value in enumerate(seasons_ids):

    # Проверяем, есть ли введенный месяц в текущем множестве
    if month in value:
        # Выводим сезон по ключу множества
        print(f'List result: {seasons_list[key]}')

    # Проходим по каждому элементу множеств уаполняем пустой словарь
    for months in value:
        # Записываем текущее значение из множества месяцов
        # в пару с сезоном по ключу множества
        seasons_dict.update({months: seasons_list[key]})

# Выводим сезон по введенному месяцу, как ключу словаря
print(f'Dict result: {seasons_dict[month]}')
