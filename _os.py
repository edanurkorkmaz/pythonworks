import os
import datetime
# result = dir(os)
# result = os.name

#dizin değiştirme
#os.chdir("C:\\")
#os.chdir("../..") iki kere üst dizine gider.


#dizin oluşturma
#os.mkdir("newdirectory")
#os.makedirs("newdirectory/yeniklasör")
# os.rename("newdirectory","yeniklasor") #isim değiştirme
# os.rmdir("nredirectory") #silme
# os.removedirs("yeniklasör/yeniklasör")



#listeleme
# result = os.listdir()

# filtreleme
# for dosya in os.listdir():
#     if dosya.endswith(".py"):
#         print(dosya)

#etkin dizi öğrenme
#result = os.getcwd()

#result = os.name # hangi işletim sistemi olduğunu gösterir.

# result = os.stat("date.py")
#result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime) # oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime) # son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime) #değiştirilme tarihi

# os.system("notepad.exe")

#path uzantılarla alakalı
# result = os.path.abspath("_os.py") konumu alıyoruz.
#result = os.path.dirname("C:/Users/Topfiyt/Desktop/python_temelleri/_os.py") konumu alınan dosyayın dizin ismini alıyoruz.
#result = os.path.dirname(os.path.abspath("_os.py"))

#result = os.path.exists("_os.py") # dosya aradığı konumda var mı yok mu ona bakar.

#result = os.path.isdir("") klasörler içindir.

#result = os.path.isfile("") dosya mı dizin mi?

#result = os.path.join("C:\\","deneme","deneme1") böyle bir path oluşturabiliriz.,

#result = os.path.split("C:\\deneme") burdada ayırırız.
#result = os.path.splitext("_os.py") # dosyanın ismiyle uzantısını ayırır.

# print(result)
