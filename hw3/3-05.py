"""Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
чисел к полученной ранее сумме и после этого завершить программу. """

res = 0

while True:
    nums = list(input('enter new nums: ').split(' '))

    for num in nums:
        if num == 'q':
            print(f'\nfinal result: {res}')
            exit()
        try:
            res = res + int(num)
        except ValueError:
            res = res

    print(f'\ntotal result: {res}\n'
          f'for exit enter \'q\'')
