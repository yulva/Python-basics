# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

print(f'Numbers from 20 to 240 which are multiples of 20 or 21 - {[n for n in range(20, 241) if n % 20 == 0 or n % 21 == 0]}')