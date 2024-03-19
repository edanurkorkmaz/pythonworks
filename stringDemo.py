website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

result = ' Hello World '.strip()     
result = ' Hello World '.lstrip()   
result = ' Hello World '.rstrip()    

#'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.

result = 'www.sadikturan.com'.strip('w.moc')

#'course' karakter dizisinin tüm karakterlerini küçük harf yapın.

result = course.lower() 
result = course.upper() 
result = course.title() 

#'website' içinde kaç tane a karakteri vardır ? (count('a'))

result = website.count('a')        
result = website.count('www')       
result = website.count('www',0,10) 

#'website' "www" ile başlayıp com ile bitiyor mu?

result = website.startswith('www')    
result = website.startswith('http')   
result = website.endswith('com')     

#'website' içinde 'com' ifadesi var mı?

result = website.find('com')         
#result = website.find('com',0,10)    
#result = course.find('Python')        
#result = course.rfind('Python')      
#result = website.index('com')         
#result = website.rindex('com')        
#result = website.rindex('comm') 

#'course' içindeki karakterlerin hepsi alfabetik mi?

result = course.isalpha()   
result = 'Hello'.isalpha()  
result = course.isdigit()   
result = '123'.isdigit()    

#'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

result = 'Contents'.center(50, '*')    
result = 'Contents'.ljust(50, '*')     
result = 'Contents'.rjust(50, '*')     

#'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.

result = course.replace(' ', '-')   
result = course.replace(' ', '-',5)  
result = course.replace(' ', '')    

#'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin

result = 'Hello World'.replace('World','There')

#'course' karakter dizisini boşluk karakterlerinden ayırın.

result = course.split(' ')  
result = result[2]          
result = result[5]          