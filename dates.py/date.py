#1
import datetime

x = datetime.datetime.now()
print(x)

#2
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

#3
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

#4
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

#5
import datetime
#Бірінші
date1 = datetime.date(2026, 2, 27)
#Екінші
date2 = datetime.date(2026, 3, 10)
#Айырмасы
difference = date2 - date1
print("Days difference:", difference.days)#11