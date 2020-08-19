# Не понял задание, поэтому сделал два варианта


# Этот выводит каждую итерацию произведения чисел
def fact1(n):
    i, res = 0, 1
    while i < n:
        i += 1
        res = res * i
        yield res


# Этот выводит просто ряд, аналог функции range()
def fact2(n):
    i = 1
    while i <= n:
        yield i
        i += 1


for el in fact1(4):
    print(el)
