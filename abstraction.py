from abc import ABC, abstractmethod 

class Hayvan(ABC): 
    def ses_cikar(self):
        pass


class Kedi(Hayvan):
    def ses_cikar(self):
        print("Miyav")


class Kopek(Hayvan):
    def ses_cikar(self):
        print("Hav Hav")

def hayvan_sesi(hayvan):
    hayvan.ses_cikar()


kedi = Kedi()
kopek = Kopek()

hayvan_sesi(kedi) 
hayvan_sesi(kopek) 
