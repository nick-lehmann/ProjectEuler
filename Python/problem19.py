# there are 100 years with twelve months each, so we have 1200 months and seven
# days a week, so: 1200 / 7 is about 171

def leapyear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

 
# monday is one, sunday 7
day = 2
month_norm = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_leap = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
fits = 0

for year in range(1901, 2001):
    if leapyear(year):
        for month in range(1, 13):
            if day % 7 == 0:
                fits += 1
            day = (day + month_leap[month]) % 7
    else:
        for month in range(1, 13):
            if day % 7 == 0:
                fits += 1
            day = (day + month_norm[month]) % 7

print fits
