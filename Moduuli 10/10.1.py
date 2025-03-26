class Hissi:
    def __init__(self, alin_kerros, ylin_kerros, hetkinen=1):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hetkinen = hetkinen

    def siirry_kerrokseen(self, kerros):
        while kerros != self.hetkinen:
            if kerros > self.hetkinen:
                self.kerros_ylös()
            else:
                self.kerros_alas()



    def kerros_ylös(self):
        self.hetkinen = self.hetkinen + 1
        print(f'Hissi on kerroksessa {self.hetkinen}')

    def kerros_alas(self):
        self.hetkinen = self.hetkinen - 1
        print(f'Hissi on kerroksessa {self.hetkinen}')

h = Hissi(1, 10)
h.siirry_kerrokseen(6)
h.siirry_kerrokseen(h.alin_kerros)