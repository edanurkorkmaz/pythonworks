website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#course dizisinde kaç karakter bulunur.
length = len(course)
print (length)

#webiste içinden www karakterlerini alın.
print(website[7:10])

#website içinden com karakterlerini alın.
length = len(website)
print(website[length-3:length])

#website içinde ilk ve son 15 karakterleri alın.
length = len(course)
print(course[0:15])
print(course[-15:])

#course içindeki karakterleri tersten yazdırın.
ters = course[::-1]
print (ters)

#bora yılmaz 32 mühendis bu karakterlerle aşağıdaki ifadeyi yazdırın.
name, surname, age, job = 'Bora','Yılmaz', 32, 'mühendis'
print("Benim adım " + name+ " " + surname+ " Yaşım "+ str(age) + " ve mesleğim "+ job)
print("Benim adım {} {}, Yaşım {} ve mesleğim {} " . format(name,surname,age,job))

# hello world ifadesinde w harfini "W" ile değiştirin.
s = "Hello world"
s = s[0:6] + "W" + s[-4:]
print(s)

#abc ifadesini yanyana 3 kere yazın.
result = "abc" *3
print(result)