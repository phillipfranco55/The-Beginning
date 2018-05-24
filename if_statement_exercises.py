# If statements to check if a year is a leap year or not.

year = input('Tell me a year to check to see if it is a leap year: ')
leap_year = int(year) % 4 == 0 and int(year) % 400 == 0
not_leap_year = int(year) % 4 != 0 and int(year) % 100 == 0 and int(year) % 400 != 0

if int(leap_year) == bool(True):
    print('It is a leap year.')
elif int(not_leap_year) == bool(False):
    print('It is not a leap year.')

print()

print(leap_year, "'If Tue it is a leap year.'")
print(not_leap_year, "'If False it is not a leap year.'")
