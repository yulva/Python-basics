# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

the_file = open("task1.txt", 'w', encoding='utf-8')

line = " "
while line:
    line = input("Write some text here or leave an empty line: ")
    the_file.write(f"{line}\n") if line != '' else the_file.close()

the_file = open('task1.txt', 'r')
content = the_file.readlines()
for line in content:
    print(line, end='')

the_file.close()
