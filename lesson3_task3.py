# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

my_func = lambda a, b, c: (a + b + c) - min(a, b, c)

print(my_func(int(input("Enter the first number: ")),
              int(input("Enter the second number: ")),
              int(input("Enter the third number: "))))