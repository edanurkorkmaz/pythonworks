class Hayvan:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    def beslen(self):
        print(f"{self.isim} besleniyor.")

    def hareket_et(self):
        print(f"{self.isim} hareket ediyor.")

class Kopek(Hayvan):
    def __init__(self, isim, yas, tur):
        super().__init__(isim, yas)
        self.tur = tur

    def havla(self):
        print("Hav hav!")

class Kus(Hayvan):
    def __init__(self, isim, yas, gaga):
        super().__init__(isim, yas)
        self.gaga = gaga

    def uc(self):
        print(f"{self.isim} uçuyor.")

class At(Hayvan):
    def __init__(self, isim, yas, renk):
        super().__init__(isim, yas)
        self.renk = renk

    def kos(self):
        print(f"{self.isim} koşuyor.")
