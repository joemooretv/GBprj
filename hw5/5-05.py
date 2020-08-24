"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
должна подсчитывать сумму чисел в файле и выводить ее на экран. """

from itertools import count

# Собираем числа от 1 до n и сразу считаем их сумму
n = 4
nums = []
nums_sum = 0
for el in count(1):
    if el > n:
        break
    else:
        nums_sum += el
        nums.append(str(el))

# Записываем в виде строки и выводим сумму на экран
with open(f'5-05-nums.txt', 'w') as file:
    file.write(' '.join(nums))
    print(f'Your data saved in \'5-05-nums.txt\' file\nTotal sum: {nums_sum}')
