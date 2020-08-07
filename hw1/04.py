n = int(input('Введи положительное число: '))

# находим последний символ как искомый
sou = n % 10

# записываем все символы, кроме последнего
rem = n // 10

# пока символы не закончатся, выполняем цикл
while rem > 0:
    # записываем предпоследний символ как сравниваемый
    comp = rem % 10
    # если сравниваемый больше искомого, обновляем искомый
    if sou < comp:
        sou = comp
    # переходим к следующему символу
    rem = rem // 10

print('Самая большая цифра: {}'.format(sou))