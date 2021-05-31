# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, x, y, *args):
        self.x = x
        self.y = y
        self.z = 'x + y * n'

    def __add__(self, other):
        print(f'The sum of z1 and z2 is')
        return f'z = {self.x + other.x} + {self.y + other.y} * n'

    def __mul__(self, other):
        print(f'Multiplication of z1 and z2 is')
        return f'z = {self.x * other.x - (self.y * other.y)} + {self.y * other.x} * n'

    def __str__(self):
        return f'z = {self.x} + {self.y} * n'


z_1 = ComplexNumber(4, -5)
z_2 = ComplexNumber(2, 3)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)
