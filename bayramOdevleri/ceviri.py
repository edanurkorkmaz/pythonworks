from googletrans import Translator

def metni_cevir(metin, cevrilen_dil):
    cevirmen = Translator()
    cevrilmis_metin = cevirmen.translate(metin, dest=cevrilen_dil)
    return cevrilmis_metin.text

def main():
    metin = input("Lütfen çevrilmek istenen metni girin: ")
    cevrilen_dil = input("Lütfen hedef dilin kodunu girin (örneğin 'en' İngilizce, 'fr' Fransızca): ")

    cevrilmis_metin = metni_cevir(metin, cevrilen_dil)
    print("Çeviri:", cevrilmis_metin)

if __name__ == "__main__":
    main()
    
