import random

class Kilpailu:
    def __init__(self, nimi, pituuskm, autot):
        self.nimi = nimi
        self.pituuskm = pituuskm
        self.autot = autot

    def tunti_kuluu(self):
        for auto in autot:
            auto.accelerate(random.randint(-10, 15))
            auto.move(1)

    def tulosta_tilanne(self):
        for i in range(10):
            print(f'{autot[i].register}, Topspeed:{autot[i].topspd}, {autot[i].currentspd}, {autot[i].distance}.')

    def kilpailu_ohi(self):
        for auto in autot:
            if auto.distance >= self.pituuskm:
                print(f'{auto.register} voitti kisan!')
                self.tulosta_tilanne()
                return True
        return False

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

kilpailu = Kilpailu('Suuri romuralli', 8000, autot)
kerrat = 1

while kilpailu.kilpailu_ohi() is False:
    kilpailu.tunti_kuluu()
    kerrat += 1
    if kerrat %10 == 0:
        kilpailu.tulosta_tilanne()




