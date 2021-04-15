# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
integer = int(input("Enter positive integer: "))
n = 0
while integer > 0:
    num = integer % 10
    if num > n:
        n = num
    integer = integer // 10
print(f"The biggest number is {n}")

