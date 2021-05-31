# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться
# с ошибкой.

class ZeroDivide:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def zero_divide(divider, denominator):
        try:
            return divider / denominator
        except:
            return f"Division by zero is not allowed."


div = ZeroDivide(20, 200)
print(ZeroDivide.zero_divide(20, 0))
print(ZeroDivide.zero_divide(20, 0.2))
print(div.zero_divide(200, 0))
