# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Start drawing {self.title}.'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Take {self.title}. Start drawing with the pen.'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Take {self.title}. Start drawing with the pencil.'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Take {self.title}. Start drawing with the marker.'


pen = Pen('a pen')
pencil = Pencil('a pencil')
handle = Handle('a marker')
print(pencil.draw())
print(handle.draw())
print(pen.draw())
