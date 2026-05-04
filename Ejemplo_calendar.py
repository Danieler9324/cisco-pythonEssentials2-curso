import calendar

print("==================  calendar  ===============================")
print(calendar.calendar(2026))

print("===================  prcal  =================================")
# prcal
calendar.prcal(2026, w=2, l=1, c=3, m=2)

print("====================  month  ================================")
# month
print(calendar.month(2026, 10))

print("===================  prmonth  ===============================")
# prmonth
calendar.prmonth(2026, 10, w=2, l=2)

print("===============  setfirstweekday  ===========================")
# setfirstweekday
calendar.setfirstweekday(calendar.SATURDAY)
calendar.prmonth(2021,12)

print("===================  weekday  ===============================")
print(calendar.weekday(2026, 4, 5))