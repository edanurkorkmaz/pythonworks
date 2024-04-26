class Sekil:
    def alan_hesapla(self):
        pass

class Dikdortgen(Sekil):
    def __init__(self, uzunluk, genislik):
        self.uzunluk = uzunluk
        self.genislik = genislik

    def alan_hesapla(self):
        return self.uzunluk * self.genislik
    
class Daire(Sekil):
    def __init__(self, yaricap):
        self.yaricap = yaricap

    def alan_hesapla(self):
        return 3.14 * (self.yaricap ** 2)
    
dikdortgen = Dikdortgen(5, 10)
dikdortgen_alan = dikdortgen.alan_hesapla()
print("Dikdörtgenin alanı:", dikdortgen_alan)

daire = Daire(4)
daire_alan = daire.alan_hesapla()
print("Dairenin alanı:", daire_alan)













        