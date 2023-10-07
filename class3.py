from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Section:
    # Класс отрезка
    def __init__(self, start1, start2):
        self.start1 = start1
        self.start2 = start2
        x1 = start1.x
        y1 = start1.y
        x2 = start2.x
        y2 = start2.y
    #Метод определения длины отрезка по формуле Пифагора
    def length_section(self):
        length_s = abs(((self.start2.x - self.start1.x) ** 2 + (self.start2.y - self.start1.y) ** 2) ** 0.5)
        print('Длина стороны - ' + str(length_s))
        return length_s

class Triangle:
    def __init__(self, ab, bc, ca):
        self.ab = ab
        self.bc = bc
        self.ca = ca

    def square(self):
        p = self.ab + self.bc + self.ca
        print('Периметр треугольника - ' + str(p))
        # В формуле используется полупериметр
        p = p / 2
        res = sqrt(p * (p - self.ab) * (p - self.bc) * (p - self.ca))
        return res


a = Point(0, 0)
b = Point(3, 0)
c = Point(0, 4)

# Три отрезка треугольника, каждый по двум точкам
section1 = Section(a, b)
section2 = Section(b, c)
section3 = Section(c, a)

# Передаем три отрезка объекту треугольник
triangle1 = Triangle(section1.length_section(), section2.length_section(), section3.length_section())
# Вычисляется площадь треугольника методом этого класса
print('Площадь треугольника по формуле Герона - '  + str(triangle1.square()))
