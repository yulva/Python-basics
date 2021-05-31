# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Cars:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f'{self.name} went.')

    def stop(self):
        print(f'{self.name} has stopped.')

    def turn(self, direction):
        print(f'{self.name} turned to the {"left" if direction == 0 else "right"}.')

    def the_speed(self):
        return f'{self.name} speed is: {self.speed}'


class TownCar(Cars):

    def the_speed(self):
        return f'{self.name} speed is: {self.speed}. Over speed!' \
            if self.speed > 60 else f'{self.name} speed is: {self.speed}'


class WorkCar(Cars):

    def the_speed(self):
        return f'{self.name} speed is: {self.speed}. Over speed!' \
            if self.speed > 40 else f'{self.name} speed is: {self.speed}'


class SportCar(Cars):
    """Sport Cars"""


class PoliceCar(Cars):

    def __init__(self, name, speed, color, is_police=True):
        super().__init__(name, speed, color, is_police)


town_car = TownCar('Kia', 30, 'white')
print(f'{town_car.name} is {town_car.color}.')
town_car.go()
print(town_car.the_speed())
town_car.turn(1)
town_car.stop()
print()

work_car = WorkCar('Volvo', 90, 'grey')
print(f'{work_car.name} is {work_car.color}.')
work_car.go()
print(work_car.the_speed())
work_car.turn(0)
work_car.stop()
print()

sport_car = SportCar('Porsche', 120, 'blue')
print(f'{sport_car.name} is {sport_car.color}.')
sport_car.go()
print(sport_car.the_speed())
sport_car.turn(1)
sport_car.stop()
print()

police_car = PoliceCar('Hyundai', 70, 'black')
police_car.go()
print(f'{police_car.name} is {police_car.color}.')
print(police_car.the_speed())
police_car.turn(0)
police_car.stop()
print()

print(f'Is {sport_car.name} a police car? It is {sport_car.is_police}.')
print(f'Is {police_car.name} a police car? It is {police_car.is_police}.')

