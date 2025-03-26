class Hissi:
    def __init__(self, tunnus, alin_kerros, ylin_kerros, hetkinen=1):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hetkinen = hetkinen
        self.tunnus = tunnus

    def siirry_kerrokseen(self, kerros):
        while kerros != self.hetkinen:
            if kerros > self.hetkinen:
                self.kerros_ylös()
            else:
                self.kerros_alas()

    def kerros_ylös(self):
        self.hetkinen = self.hetkinen + 1
        print(f'{self.tunnus}Hissi on kerroksessa {self.hetkinen}')

    def kerros_alas(self):
        self.hetkinen = self.hetkinen - 1
        print(f'{self.tunnus}Hissi on kerroksessa {self.hetkinen}')

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissi_määrä):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissi_määrä = hissi_määrä
        self.hissit = []
        for i in range(self.hissi_määrä):
            self.hissit.append(Hissi(f'{i+1}', f'{alin_kerros}',f'{ylin_kerros}'))

    def aja_hissiä(self, tunnus, kerros):
        if kerros < self.alin_kerros or kerros > self.ylin_kerros:
            print('Pyydettyä hissin kerrosta ei ole')
        else:
            self.hissit[tunnus-1].siirry_kerrokseen(kerros)

kerrostalo1 = Talo(1,12,3)
kerrostalo1.aja_hissiä(2, 10)
