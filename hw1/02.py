time = int(input('Введи время в секундах: '))
sec = time % 60
min = time // 60
hour = min // 60
print("{:02d}:{:02d}:{:02d}".format(hour, min % 60, sec))
