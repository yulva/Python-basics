# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary
        self.bonus = bonus


class Position(Worker):
    def __init__(self, name, surname, position, salary, bonus):
        super().__init__(name, surname, position, salary, bonus)
        self.__income = {'salary': salary, 'bonus': bonus}

    def full_name(self):
        return self.name + self.surname

    def full_income(self):
        return f'{sum(self.__income.values())}'


accountant = Position('Vasya ', 'Pupkin', 'accountant', 20000, 5000)
print(accountant.full_name())
print(accountant.full_income())
print(accountant.position)
