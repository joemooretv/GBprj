def user_info(name, surname, birth, city, email, tel):
    print(f'{name} {surname}, {birth}\n'
          f'{city}\n'
          f'{email}, {tel}')


user_info(birth='06.06.1966', name='John', email='test@est.ru',
          surname='Doe', city='Nahodka', tel='89996669966')