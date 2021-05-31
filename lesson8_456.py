# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.


class WarehouseOffice:

    def __init__(self, name, price, quantity, lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.list = lists
        self.shop_full = []
        self.my_shop = []
        self.product = {'Device model': self.name, 'Price per one': self.price, 'Quantity': self.quantity}

    def __str__(self):
        return f'{self.name} price {self.price} quantity {self.quantity}'

    def reception(self):

        try:
            unit = input(f'Enter the name: ')
            unit_p = int(input(f'Enter the price per one '))
            unit_q = int(input(f'Enter quantity '))
            unique = {'Device model': unit, 'Price per one': unit_p, 'Quantity': unit_q}
            self.product.update(unique)
            self.my_shop.append(self.product)
            print(f'Current list is -\n {self.my_shop}')
        except:
            return f'Data entry error!'

        print(f'To quit - Q, To continue - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.shop_full.append(self.my_shop)
            print(f'The entire warehouse -\n {self.shop_full}')
            return f'Exit'
        else:
            return WarehouseOffice.reception(self)


class Printer(WarehouseOffice):
    def to_print(self):
        return f'to print a document {self.list} times'


class Scanner(WarehouseOffice):
    def to_scan(self):
        return f'to scan a document {self.list} times'


class Copier(WarehouseOffice):
    def to_copy(self):
        return f'to copy a document  {self.list} times'


unit_1 = Printer('Cannon', 800, 4, 20)
unit_2 = Scanner('Epson', 5600, 9, 8)
unit_3 = Copier('HP', 1300, 3, 34)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copy())