#leap or not

def leap_year():
    year = int(input())
    if (year%4 == 0 and year%100 != 0)or(year%400 == 0):
        print(True)
    else:
        print(False)
leap_year()
