def my_func(x, y):
    res = x
    for i in range(y):
        res = res * x
    return res


print(my_func(2, 3))
