# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open("task2.txt", encoding='utf-8') as file:
    lines = file.readlines()
    for number, weight in enumerate(lines, 1):
        words = len(weight.split())
        print(f"Line number {number} has {words} words.")
