def is_leap(year):
    if year % 100 == 0:
        return year % 400 == 0
    else: 
        return year % 4 == 0


year = input('Please enter a 4 digits of year: ')

while len(year) != 4:
    year = input('Please enter a 4 digits of year: ')

year = int(year)

if is_leap(year):
    print("The year you have entered is a leap year")
else:
    print("The year you have entered is not a leap year")

