def my_func(a, b, c):
    res = [a, b, c]
    res.remove(min(res))
    return sum(res)


print(my_func(3, 3, 1))
