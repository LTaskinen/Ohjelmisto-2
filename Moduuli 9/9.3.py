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

auto1 = Auto('ABC-123', 142)
auto1.accelerate(60)
auto1.move(1.5)
print(auto1.distance)