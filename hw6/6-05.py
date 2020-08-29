class Stationery:
    title: str = None

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    title: str = 'Pen'

    def draw(self):
        print('Пишу ручкой')


class Pencil(Stationery):
    title: str = 'Pencil'

    def draw(self):
        print('Рисую карандашом')


class Marker(Stationery):
    title: str = 'Marker'

    def draw(self):
        print('Закрашиваю маркером')


s1 = Stationery()
s2 = Pen()
s3 = Pencil()
s4 = Marker()

print(s1, s1.title)
s1.draw()
print(s2, s2.title)
s2.draw()
s3.draw()
s4.draw()
