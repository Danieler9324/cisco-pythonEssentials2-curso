from datetime import date
import time

# Date
print("----------------- Uso de date  --------------------")
hoy = date.today()

print("Hoy:", hoy)
print("Año:", hoy.year)
print("Mes:", hoy.month)
print("Dia:", hoy.day)


# Time
print("----------------- Uso de time  --------------------")
timestamp = time.time()
print("Marca de tiempo:", timestamp)

dia = date.fromtimestamp(timestamp) 
print("Fecha:", dia)

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
