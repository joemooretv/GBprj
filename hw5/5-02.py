"""Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке."""

with open('5-02-text.txt') as file:
    i = 1
    words_len = {}

    # Собираем пары "номер строки: количество слов"
    for line in file:
        words_len.update({i: len(line.strip().split(' '))})
        i += 1

    # Считаем количество строк и выводим
    lines_len = len(words_len)
    print(f'{lines_len} lines total \n')

    # Выводим пары из словаря words_len
    for k, v in words_len.items():
        print(f'line {k}: {v} word(s)')
