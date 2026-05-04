import calendar                                                                         # Clases para la creacion de calendarios
                                                                                        #  -calendar.Calendar: otorga metodos para preparar datos de calendario y dar formato
print("==================  calendar  ===============================")                  #  -calendar.TextCalendar: se usa para crear calendario de texto regulares                            
print(calendar.calendar(2026))                                                          #  -calendar.HTMLCalendar: se utiliza para crear calendarios HTML
                                                                                        #  -calendar.LocalTextCalendar: es una subclase de la clase calendar.TextCalendar. 
print("===================  prcal  =================================")                  #                               El constructor de esta clase toma el parámetro locale,                          
                                                                                        #                               el cual se utiliza para devolver los nombres 
calendar.prcal(2026, w=2, l=1, c=3, m=2)                                                #                               apropiados de los meses y días de la semana.
                                                                                        #  -calendar.LocalHTMLCalendar: tecnicamente es lo mismo que LocalTextCalendar pero
print("====================  month  ================================")                  #                               ahora es la subclase de calendar.HTMLCalendar
print(calendar.month(2026, 10))

print("===================  prmonth  ===============================")
calendar.prmonth(2026, 10, w=2, l=2)

print("===============  setfirstweekday  ===========================")
calendar.setfirstweekday(calendar.SATURDAY)
calendar.prmonth(2021,12)

print("===================  weekday  ===============================")
print(calendar.weekday(2026, 4, 5))

print("==================  weekheader  =============================")
print(calendar.weekheader(2))

print("===============  isleap/leapdays  ===========================")
print(calendar.isleap(2020))
print(calendar.leapdays(2010, 2026))

print("=================  iterweekdays  ============================")
c = calendar.Calendar(calendar.SUNDAY)  # 0 = MONDAY, 1 = TUESDAY, 2 = WEDNESDAY, 3 = THURSDAY, 4 = FRIDAY,  5 = SATURDAY, 6 = SUNDAY

for weekday in c.iterweekdays():
    print(weekday, end=" ")   # = 6, 0, 1, 2, 3, 4, 5

print("\n==================  itermonthdates  =======================")
ca = calendar.Calendar()

for fecha in ca.monthdatescalendar(2020,11):
    print(fecha, end=" \n" )

print("\n==============  itermonthdays (2,3,4)  ====================")

for itera in ca.itermonthdays(2020, 11):
    print(itera, end=" ")

print("\n")
for itera in ca.itermonthdays2(2020, 11):
    print(itera, end=" ")

print("\n")
for itera in ca.itermonthdays3(2020, 11):
    print(itera, end=" ")

print("\n")
for itera in ca.itermonthdays4(2020, 11):
    print(itera, end=" ")

print("\n===============  monthdays2calendar  ======================")

for data in ca.monthdays2calendar(2020,11):
    print(data)