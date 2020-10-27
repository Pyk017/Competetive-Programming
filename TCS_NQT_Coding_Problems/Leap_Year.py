def check_year(year):

    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return  False


_year = int(input())
print("It is a Leap Year") if check_year(_year) else print("It is not a Leap Year")
