def div2num(num_1, num_2):
    try:
        return round(num_1 / num_2, 2), round(num_2 / num_1, 2)
    except ZeroDivisionError:
        if num_1 == 0:
            return 0, None
        else:
            return None, 0
    except TypeError:
        return 'Ошибка: функция принимает только числа'


print(div2num(666, 6))
