import re


class NotNumber(Exception):

    def __str__(self):
        return 'That\'s not a numbers.'


res = []
print('Press \'ctrl + D\' to complete your list.')

while True:
    try:
        num = input('Enter new number: ')
        # если в строке есть символы, вызываем ошибку
        if re.sub(r'[^\w\S]+|[\d]+', r'', num.strip()):
            raise NotNumber
        res.append(int(num))
    except EOFError:
        print(f'Done! Your list: {res}')
        exit()
    except NotNumber:
        print('Not added. Please, print numbers only.')
