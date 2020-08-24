"""Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
окончании ввода данных свидетельствует пустая строка. """

from datetime import datetime

# Создаем пустой список и наполняем
# пока пользователь не введет пустую строку
content = []
while True:
    line = input('Enter text line to save:\n')
    if not line:
        break
    content.append(line + '\n')

# Получаем текущие дату и время
dt = datetime.now().strftime("_%d.%m.%Y_%H:%M:%S")

# Сохраняем в файл
with open(f'list{dt}.txt', 'w') as file:
    file.writelines(content)
    print(f'Your data saved in \"list{dt}.txt\" file')
