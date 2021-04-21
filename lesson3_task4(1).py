# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def my_func(x, y):
    try:
        res = x ** y
    except TypeError:
            return "Enter one real positive integer and one negative integer!"
    return res

print(my_func(int(input("Enter one real positive integer: ")),
              int(input("Enter one negative integer: "))))
