# Bir cümle alıp, bu cümlenin içinde belirli bir kelimenin kaç kez geçtiğini bulun.
# Ardından cümledeki bütün kelimeleri ayırarak, her bir kelimenin baş harflerinibüyük harf yapın. 
# Ayrıca cümlenin başındaki ve sonundaki gereksiz boşlukları kaldırın.

# cumle = "Python programlama dili çok güçlüdür.Python, veri bilimi, yapay zeka ve daha birçok alanda tercih edilir."

# sonuc = cumle.count("yapay")
# sonuc = cumle.split()
# sonuc = cumle.title()
# sonuc1 = sonuc.split()
# print(sonuc1)

# Bir metin verildiğinde, metindeki her bir kelimenin uzunluğunu bulun. 
# Ardından en uzun kelimeyi ve uzunluğunu çıkartın. 
# Ayrıca, bu uzun kelimeyi metindeki tüm kelimelerle karşılaştırarak, 
# metin içerisinde kaç kez geçtiğini belirleyin.


metin = "Python, programlama dilleri arasında çok popülerdir. Python öğrenmek eğlencelidir ve Python ile çeşitli projeler yapabilirsiniz."

kelimeler = metin.split()
kelime_uzunluklari = {kelime: len(kelime) for kelime in kelimeler}

en_uzun_kelime = max(kelime_uzunluklari, key=kelime_uzunluklari.get)
en_uzun_uzunluk = kelime_uzunluklari[en_uzun_kelime]

en_uzun_kelime_sayisi = kelimeler.count(en_uzun_kelime)

print("En Uzun Kelime:", en_uzun_kelime)
print("Uzunluğu:", en_uzun_uzunluk)
print("Metinde Kaç Kez Geçiyor:", en_uzun_kelime_sayisi)


  
