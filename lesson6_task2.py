# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        # self._depth = _depth
        # self._weight = _weight

    def result(self, depth=5, weight=25):
        result = self._length * self._width * depth * weight / 1000
        print(f'You need {result} tons for the road.')


village_road = Road(20, 5000)
village_road.result()
