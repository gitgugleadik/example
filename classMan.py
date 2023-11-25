class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 10
        self.food = 10
        self.money = 0

    def __str__(self):
        return 'Я - {}, сытость - {}, еды - {}, денег - {} '.format(
            self.name, self.fullness, self.food, self.money)
    def eat(self):
        if self.food > 10:
            print('{} поел '.format(self.name))
            self.fullness +=10
            self.food -=10
        else:
            print('{} Нет еды'.format(self.name))

    def work(self):
        print('{} сходил на работу '.format(self.name))
        self.money += 50
        self.fullness -= 10

man = Man(name = 'Jack')
print(man)