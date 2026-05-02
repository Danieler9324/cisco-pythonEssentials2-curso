from datetime import date
from datetime import time
from datetime import datetime
import time as tm

# Date
print("----------------- Uso de date  --------------------")
hoy = date.today()

print("Hoy:", hoy)
print("Año:", hoy.year)
print("Mes:", hoy.month)
print("Dia:", hoy.day)


# Time
print("----------------- Uso de time  --------------------")
timestamp = tm.time()
print("Marca de tiempo:", timestamp)

dia = date.fromtimestamp(timestamp) 
print("Fecha:", dia)

t = time(14, 53, 20, 1)

print("Tiempo:", t)
print("Hora:", t.hour)
print("Minutos:", t.minute)
print("Segundos:", t.second)
print("Microsegundo:", t.microsecond)

# timestamp
print("-------- timestamp -------------")
dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp())
    
# ctime
print("-------- ctime  -------------")
timestamp = 1572879180
print(tm.ctime(timestamp))

# struct_time
print("-------- struct_time  -------------")                                        
timestamp = 1572879180
st = tm.gmtime(timestamp)

print(tm.asctime(st))
print(tm.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))  # <--- tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdts  

print("-------- strftime con datetime -------------")  
d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))

print("-------- strftime con time -------------")
timestamp = 1572879180
st = tm.gmtime(timestamp)

print(tm.strftime("%Y/%m/%d %H:%M:%S", st))
print(tm.strftime("%Y/%m/%d %H:%M:%S"))

# Replace
print("----------------- Uso de replace  --------------------")
dia2 = date(1991, 2, 5)
print(dia2)

dia2 = dia2.replace(year=1992, month=1, day=16)
print(dia2)

# weekday y isoweekday
print("----------------- Uso de weekday  --------------------")
dia3 = date(1991, 2, 5)
print(dia3.weekday())

print("----------------- Uso de isoweekday  -----------------")
print(dia3.isoweekday())