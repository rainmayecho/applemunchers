##or You could 1200/7 and be a fruitcake =)

sundays = 0
week = [1,2,3,4,5,6,7]
month_31 = [1,3,5,7,8,10,12]
month_30 = [4,6,9,11]
feb = 2
init = 2
day = init
ly = False


def calc_day(month, day):
    temp = day+month%7
    if temp > 7:
        return temp%7
    else:
        return temp

for year in range(1900,2001):
    if year%4 == 0:
        ly = True
        if year%1000 ==0:
            if not year%400 == 0:
                ly = False
    for month in range(1,13):
        if month in month_31:
            if day == week[0] and year > 1900:
                sundays+=1
            day = calc_day(31,day)
        if month in month_30:
            if day == week[0] and year > 1900:
                sundays+=1
            day = calc_day(30,day)
        if month == feb:
            if day == week[0] and year > 1900:
                sundays+=1
            if ly:
                day = calc_day(29,day)
            else:
                day = calc_day(28,day)
print sundays

    
