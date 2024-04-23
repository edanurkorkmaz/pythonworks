from googletrans import Translator
import sys

def metni_cevir(metin, cevrilen_dil):
    cevirmen = Translator()
    try:
        cevrilmis_metin = cevirmen.translate(metin, dest=cevrilen_dil)
        return cevrilmis_metin.text
    except Exception:
        return None 

def main():
    try:
        metin = input("Lütfen çevrilmek istenen metni girin: ")

        cevrilen_dil = input("Lütfen hedef dilin kodunu girin (örneğin 'en' İngilizce, 'fr' Fransızca): ")
        
        cevrilmis_metin = metni_cevir(metin, cevrilen_dil)
        
        if cevrilmis_metin is None:
            print("Çevrilecek dili yanlış girdiniz. Lütfen tekrar deneyin.") 
        else:
            print("Çeviri:", cevrilmis_metin) 
            
    except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
