min = 00
hour = 00
time = int(input('Введи время в секундах: '))
sec = time % 60
if 1 <= time / 60:
    min = time // 60
    if min > 59:
        min = min % 60
        hour = min // 60
print("{}:{}:{}".format(hour, min, sec))
