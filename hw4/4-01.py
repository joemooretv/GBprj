from sys import argv


def salary(hours, price, extra):
    return int(hours) * int(price) + int(extra)


try:
    script, a, b, c = argv
    print(salary(int(a), int(b), int(c)))
except ValueError:
    print('wrong argument format')

print((22 * 33) + 7)
