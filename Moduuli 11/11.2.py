import random

class Auto:
    def __init__(self, register, topspd, currentspd=0, distance=0):
        self.register = register
        self.topspd = topspd
        self.currentspd = currentspd
        self.distance = distance
    def accelerate(self, kmh):
            self.currentspd = self.currentspd + kmh
            if self.currentspd > self.topspd:
                self.currentspd = self.topspd
            elif self.currentspd < 0:
                self.currentspd = 0
            return
    def move(self, h):
        self.distance = self.distance + h*self.currentspd
        return

class Sähköauto(Auto):
    def __init__(self, register, topspd, battery, currentspd, distance):
        self.battery = battery
        super().__init__(register, topspd, currentspd, distance)

class Polttomoottoriauto(Auto):
    def __init__(self, register, topspd, tank, currentspd, distance):
        self.tank = tank
        super().__init__(register, topspd, currentspd, distance)

autot = []
autot.append(Sähköauto('ABC-15',180,52.5, 130,0))
autot.append(Polttomoottoriauto('ACD-123',165,32.3, 135,0))
for auto in autot:
    auto.accelerate(random.randint(-10, 15))
    auto.move(3)
for auto in autot:
    print(f'{auto.register}:{auto.distance}km')