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

d = date.fromtimestamp(timestamp)
print("Fecha:", d)

# Replace
print("----------------- Uso de replace  --------------------")
d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)
    