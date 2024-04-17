from datetime import datetime
from datetime import timedelta
#from datetime import datetime
# from datetime import date
# from datetime import time

# import datetime
simdi = datetime.now()
# # result = dir(datetime.time)
# # result = dir(datetime.date)
# # result = simdi.year
# # result = simdi.day
# # result = datetime.ctime(sımdı)
# # result = datetime.strftime(sımdı,"%Y")
# # result = datetime.strftime(sımdı,"%X")
# # result = datetime.strftime(sımdı,"%d")
# # result = datetime.strftime(sımdı,"%A")
# # result = datetime.strftime(sımdı,"%B %Y %X")

# # t = "23 Mart 2000"

# # gun, ay, yil = t.split()
# # print(gun)
# # print(ay)
# # print(yil)

# t = "15 April 2019 hour 10:12:30"

# result = datetime.strptime(t, "%d %B %Y hour %H:%M:%S")
# result = result.year

# birthday = datetime(1983,5,9,12,30,00)
# result = datetime.timestamp(birthday) #saniye
# result = datetime.fromtimestamp(result) #saniye to datetime
# result = datetime.fromtimestamp(0)
# result = simdi - birthday # timedelta 

# result = result.seconds
print(simdi)
result = simdi + timedelta(seconds=10)

print(result)




