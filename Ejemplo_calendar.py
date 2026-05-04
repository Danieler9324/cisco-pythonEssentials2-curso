import calendar
print(calendar.calendar(2026))

print("============================================================================")
# prcal
calendar.prcal(2026, w=2, l=1, c=3, m=2)

print("============================================================================")
# month
print(calendar.month(2026, 10))

print("============================================================================")
# prmonth
calendar.prmonth(2026, 10, w=2, l=2)

print("============================================================================")
# setfirstweekday

calendar.setfirstweekday(calendar.SATURDAY)
calendar.prmonth(2021,12)