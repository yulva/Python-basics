# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func(a, b):
    try:
        a, b = int(a), int(b)
        c = a / b
        return round(c, 4)
    except ZeroDivisionError:
        return "You can not divide by zero!"
    except ValueError:
        return "Only numbers!"

print(my_func(input("Specify a - "), input("Specify b - ")))

