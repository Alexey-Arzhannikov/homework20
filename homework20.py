class Car:
    def __init__(self):
        self.price = 1000000
        self.hp = 100
    def horse_powers(self):
        print(self.hp)

class Nissan(Car):
    def __init__(self):
        self.price = 1500000
        self.hp = 250

class Kia(Car):
    def __init__(self):
        self.price = 1250000
        self.hp = 150

kia = Kia()
kia.horse_powers()
nissan = Nissan()
nissan.horse_powers()

