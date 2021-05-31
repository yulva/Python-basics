# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

while True:
    the_str = input("Please enter several words separated by spaces: ")
    if len(the_str) < 3 or the_str.count(' ') < 2:
        print("Wrong, try again: ")
        continue

    break

for index, word in enumerate(the_str.split()):
    print(index + 1, (word, word[:10])[len(word) > 10])
