# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_func(**kwargs):
     return ' '.join(kwargs.values())
print(my_func(name=input("Enter your name: "),
              surname=input("Enter your surname: "),
              year=input("Enter your year of birth: "),
              city=input("Enter your city: "),
              email=input("Enter your email: "),
              telephone=input("Enter your telephone: ")))