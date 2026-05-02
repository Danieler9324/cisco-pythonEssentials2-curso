from datetime import datetime
from datetime import date
from datetime import time
import time as tm

dt = datetime(2020, 11, 4, 14, 53)

# 2020/11/04 14:53:00:
print(dt)

# 20/November/04 14:53:00 PM:
print(dt.strftime("%y/%B/%d %H:%M:%S"))

# Wed, 2020 Nov 04:
print(dt.strftime("%a, %Y %b %d"))

# Wednesday, 2020 November 04:
print(dt.strftime("%A, %Y %B %d"))

# Día de la semana: 3
print(dt.strftime( "Dia de la semana: %w ")) 

# Día del año: 309
print(dt.strftime("Dia del año: %j"))

# Número de semana en el año: 44
print(dt.strftime("Numero de semana en el año: %W"))