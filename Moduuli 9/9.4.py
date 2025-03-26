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

autot = []
for i in range(10):
    autot.append(Auto(f'ABC-{i + 1}', random.randint(100, 200)))

while autot[i].distance < 10000:
    for i in range(10):
        autot[i].accelerate(random.randint(-10,15))
    for i in range(10):
        autot[i].move(1)
        if autot[i].distance >= 10000:
            print(f'{autot[i].register} voitti kisan!')
            break



for i in range(10):
        print(f'{autot[i].register}, Topspeed:{autot[i].topspd}, {autot[i].currentspd}, {autot[i].distance}.')
