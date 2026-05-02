# Escribe un programa que cree un objeto datetime para el 4 de noviembre de 2020, 14:53:00. El objeto creado debe llamar al método strftime 
# con el formato apropiado para mostrar el siguiente resultado:

# 2020/11/04 14:53:00               ya
# 20/November/04 14:53:00 PM        ya
# Wed, 2020 Nov 04                  ya
# Wednesday, 2020 November 04       ya
# Día de la semana: 3               ya
# Día del año: 309                  ya
# Número de semana en el año: 44    
# Nota: Cada línea de resultado debe crearse llamando al método strftime con al menos una directiva en el argumento de formato.
from datetime import datetime
from datetime import date
from datetime import time
import time as tm

dt = datetime(2020, 11, 4, 14, 53)

print(dt)
print(dt.strftime("%y/%B/%d %H:%M:%S"))
print(dt.strftime("%a, %Y %b %d"))
print(dt.strftime("%A, %Y %B %d"))
print("Dia de la semana: ", dt.weekday() + 1) 
print("Dia del año: ", dt.strftime("%j"))
print("Numero de semana en el año: ", dt.strftime("%W"))