class Date:
    day: int
    month: int
    year: int

    def __init__(self, date: str):
        date = self.date_to_int(date)
        self.date_validate(date)
        self.day, self.month, self.year = date[0], date[1], date[2]

    @staticmethod
    def date_validate(date):
        if len(date) != 3:
            raise ValueError('You need 3 dates in format \'DD-MM-YY\'')
        elif 1 < date[2] > 99:
            print(date[2])
            raise ValueError('Year must be in YY format')
        elif 1 < date[1] > 12:
            raise ValueError('There are only 12 months in year')

    @classmethod
    def date_to_int(cls, string: str):
        try:
            string = string.split('-')
            dates = [int(num) for num in string]
        except ValueError:
            return 'format must be \'DD-MM-YY\''
        return dates


a = Date('01-11-20')
print(f'{a.day:02d}-{a.month:02d}-{a.year:02d}')
