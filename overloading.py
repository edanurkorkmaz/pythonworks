class sekil:
    def alan(self, sekil_tip, *args):
        if sekil_tip == "daire":
            yaricap = args[0]
            return 3.14 * (yaricap ** 2)
        elif sekil_tip == "dikdörtgen":
            uzunluk = args[0]
            genislik = args[1]
            return uzunluk * genislik
        else:
            raise ValueError("Geçerli olmayan şekil")

sekil = sekil()

print("daire alanı:", sekil.alan("daire", 5))  
print("dikdörtgen alanı:", sekil.alan("dikdörtgen", 5, 10))  
