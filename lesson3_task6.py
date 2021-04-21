# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(words):
    letters = "abcdefghijklmnopqrstuvwxyz"
    return words.title() if not set(words).difference(letters) else f"Enter words in lowercase Latin letters!"


terms = input("Enter words in lowercase Latin letters: ").split()
for x in terms:
    answer = int_func(x)
    if answer:
        print(int_func(x), ' ')