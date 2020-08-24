"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10
строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
средней величины дохода сотрудников."""

# Читаем все значения
with open('5-03-salary.txt') as file:
    pairs = [line.replace('\n', '').split(' ') for line in file]

total_salary = 0

print('Employees with < 20.000 salary:')
for k, v in pairs:

    # Выводим сотрудников с зарплатой < 20.000
    if float(v) < 20000:
        print(f'- {k}')

    # Считаем зарплатный фонд
    total_salary += float(v)

average_salary = total_salary / len(pairs)

print(f'\nAverage salary: {round(average_salary, 2)}')
