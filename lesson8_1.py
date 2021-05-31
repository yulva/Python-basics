# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Data:
    def __init__(self, d_m_y):
        self.d_m_y = str(d_m_y)

    @classmethod
    def extract(cls, d_m_y):
        the_date = []

        for i in d_m_y.split():
            if i != '-':
                the_date.append(i)
        return int(the_date[0]), int(the_date[1]), int(the_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'All right'
                else:
                    return f'Wrong year!'
            else:
                return f'Wrong month!'
        else:
            return f'Wrong day!'

    def __str__(self):
        return f'The current date is {Data.extract(self.d_m_y)}'


today = Data('24 - 05 - 2021')
print(today)
print(Data.valid(32, 12, 2020))
print(Data.valid(3, 8, 2002))
print(Data.extract('5 - 12 - 2021'))
print(today.valid(9, 13, 2011))
print(today.extract('4 - 1 - 2017'))


