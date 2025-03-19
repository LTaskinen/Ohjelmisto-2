class Auto:
    def __init__(self, register, topspd, currentspd=0, distance=0):
        self.register = register
        self.topspd = topspd
        self.currentspd = currentspd
        self.distance = distance
auto1 = Auto('ABC-123', 142)
print(f'{auto1.register}, {auto1.topspd}, {auto1.currentspd}, {auto1.distance}')