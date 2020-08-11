i = 0
q = '+'
items = []

while True:
    # Запрашиваем данные у пользователя
    name = input('Введите название: ')
    price = input('Введите цену: ')
    amount = input('Введите количество: ')
    unit = input('Введите единицу измерения: ')
    i += 1

    # Формируем кортеж
    item = (i, {'название': str(name),
                'цена': int(price),
                'количество': int(amount),
                'ед': str(unit)})

    # Добавляем картеж в список товаров
    items.append(item)

    print(f'Товар {name} добавлен в список.')
    q = input('Чтобы добавить еще один товар, введите \'+\': ')

    # Завершаем цикл, когда требуется

    if q != '+':
        break

# Создаем пустой список для результатов анализа
an = dict()
# Проходим по всем полученным товарам
for el in items:
    # Получаем пары ключ-значение для элементов с индексом 1 (картежей) и идем по ним
    for k, v in el[1].items():
        # В словарь 'an' добавляем уникальный ключ, если его еще нет
        # В качестве значения ключа создаем пустой список
        if not an.get(k):
            an.update({k: []})
        # Если по ключу в словаре 'an' еще нет значения, добавляем его в список
        if an[k].count(v) == 0:
            an[k].append(v)
print(an)