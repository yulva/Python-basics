# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def my_func(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return "Enter one real positive integer and one negative integer!"
        else:
            answer = 1
            for _ in range(abs(y)):
                answer /= x
                return f"The answer is {round(answer, 4)}"
    except ValueError:
        return "Enter one real positive integer and one negative integer!"


print(my_func(input("Enter one real positive integer: "),input("Enter one negative integer: ")))