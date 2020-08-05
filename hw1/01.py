name = str(input('как тебя зовут? '))
age = int(input('Сколько тебе лет? '))
if 4 < age < 21:
    years = 'лет'
else:
    if age % 10 == 1:
        years = 'год'
    elif 1 < age % 10 < 5:
        years = 'года'
    else:
        years = 'лет'
print(name, ', тебе', age, years)
