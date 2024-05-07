class Product:
    #method
    #attribute,property
    def __init__(self,name,price,isActive):
        self.name = name
        self.price = price
        self.isActive = isActive
# instance,object
p1 = Product("ıphone 15","50000",True)
p2 = Product("ıphone 15 pro","70000",True)
p3 = Product("Samsung s24","80000",False)

urunler = [p1, p2, p3]

for urun in urunler:
    if urun.isActive:
        print(f"ürün adı: {urun.name} ürün fiyatı {urun.price}")



