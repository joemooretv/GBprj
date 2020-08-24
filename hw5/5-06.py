from re import compile

result = {}

with open('5-06-subj.txt', 'r') as file:
    for line in file:
        # Фильтр символов
        filter1 = compile('[^a-zA-Zа-яА-Я0-9 ]')
        # Фильтр букв
        filter2 = compile('[^0-9 ]')

        # Записываем в переменную предмет
        elems = filter1.sub('', line).split(' ')
        subj = elems.pop(0)

        # Считаем общий балл
        mark = 0
        for num in elems:
            num = filter2.sub('', num)
            if num != '':
                mark += int(num)

        # Заполняем словарь
        result.update({subj: mark})

print(result)
