# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма ((2 * H + 0.3)/100). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Fabric(ABC):
    result = 0

    def __init__(self, fluent):
        self.fluent = fluent

    @property
    @abstractmethod
    def usage(self):
        pass

    def __add__(self, other):
        Fabric.result += self.usage + other.usage
        return Suit(0)

    def __str__(self):
        res = Fabric.result
        Fabric.result = 0
        return f"{res}"


class Coat(Fabric):
    @property
    def usage(self):
        return round((self.fluent / 6.5) + 0.5)


class Suit(Fabric):
    @property
    def usage(self):
        return round((2 * self.fluent + 0.3) / 100)


coat = Coat(50)
suit = Suit(180)
print(coat + suit + coat)



