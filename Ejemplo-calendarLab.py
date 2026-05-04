# Crea una clase llamada MyCalendar que se extiende de la clase Calendar.
# Crea el método count_weekday_in_year con los parámetros de year y weekday. El parámetro weekday debe tener un valor entre 0 y 6, donde 0 es el lunes y 6 es el domingo. 
# El método debe devolver el número de días como un número entero.
# En tu implementación, usa el método monthdays2calendar de la clase Calendar.
import calendar

class MyCalendar(calendar.Calendar):
    def __init__(self):
        super().__init__()
    
    def count_weekday_in_year(self, year, weekday):
        count= 0

        for month in range (1, 13):
            month_data = self.monthdays2calendar(year,month)

            for week in month_data:
                for day, wd in week:
                    if day != 0 and wd == weekday:
                        count +=1
    
        return count
    
cal = MyCalendar()
print(cal.count_weekday_in_year(2020,0))  # 0 = MONDAY, 1 = TUESDAY, 2 = WEDNESDAY, 3 = THURSDAY, 4 = FRIDAY,  5 = SATURDAY, 6 = SUNDAY