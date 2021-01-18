import datetime

day = datetime.datetime(1901, 1, 1)
endDate = datetime.datetime(2000, 12, 31)
day += datetime.timedelta(days = 6 - day.weekday())

count = 0
while(day < endDate):
    if(day.day == 1):
        count += 1
    day += datetime.timedelta(days = 7)

print(count)

assert count == 171
