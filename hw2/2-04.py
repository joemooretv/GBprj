words = str(input('Введите слова через пробел: ')).replace('.', '').split(' ')

i = 1

for el in words:

    if len(el) > 10:
        el = el[:10] + '...'

    print(f'{i}. {el}')
    i += 1
