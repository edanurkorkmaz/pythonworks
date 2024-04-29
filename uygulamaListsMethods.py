customers = ["sadikturan","ahmetyilmaz","cinarturan","yigitbilgi"]
order_totals = [12000,13000,5000,15000]

# customers.append("edanurkorkmaz")
# order_totals.append("5000")

# customers.pop()
# order_totals.pop()

# sonuc = f"{customers[0]} isimli müşterinin sipariş toplamı {order_totals[0]}liradır"
# sonuc1 = f"{customers[1]} isimli müşterinin sipariş toplamı {order_totals[1]}liradır"
# sonuc2 = f"{customers[2]} isimli müşterinin sipariş toplamı {order_totals[2]}liradır"
# sonuc3 = f"{customers[3]} isimli müşterinin sipariş toplamı {order_totals[3]}liradır"

# print(sonuc)
# print(sonuc1)
# print(sonuc2)
# print(sonuc3)

# customers.sort()
# order_totals.sort()
# order_totals.reverse()
# print(order_totals)
# print(customers)
# sonuc = min(order_totals)
# print(sonuc)
# print(customers)
# print(order_totals)

# sonuc = customers.count("sadikturan")
# print(sonuc)

# customers.remove("ahmetyilmaz")
# print(customers)

# customers.clear()
# order_totals.clear()

username = input("ad: ")
toplam = input("toplam: ")

customers.append(username)
order_totals.append(toplam)

print(customers)
print(order_totals)