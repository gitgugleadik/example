# Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель",
# наслідувані від "Транспортний засіб". Наповніть класи атрибутами на свій розсуд.

class Vehicle:
    speed = 10
    color = 'red'
    name = ''

    def Info(self):
        res = f'my {self.name} and  my speed {self.speed} and my color {self.color}'
        return res


car = Vehicle()
car.name = 'AUDI'
car.color = 'green'
print(car.name and car.Info())

Plane = Vehicle()
Plane.name = 'Boing 747'
Plane.color = 'blu'
print(Plane.name and Plane.Info())

ship = Vehicle()
ship.name = 'Colorado'
ship.color = 'black'
print(ship.name and ship.Info())