from datetime import date
from datetime import time
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
