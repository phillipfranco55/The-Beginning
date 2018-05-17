

# Program to find the average of the number of hours slept.
hours_slept = 6.2 + 7 + 8 + 5 + 6.5 + 7.1 + 8.5
days_slept = 7
avg_hours_slept = hours_slept / days_slept
print("The average number of hours slept is", avg_hours_slept)

# Is 297 divisible by 3?
print("Is 297 divisible by 3?")
two_ninety_seven = 297 % 3
print("297 % 3 =", two_ninety_seven, "so yes.")

# What is 2 raised to the tenth power?
print("2 raised to the tenth power is:", 2 ** 10)

# Are the years, 1800, 1900, 1903, and 2002 leap years?
year_1800 = 1800 % 400  # Divisible by 100 but not 400
year_1900 = 1900 % 400  # Divisible by 100 but not 400
year_1903 = 1903 % 4    # Not divisible by 4
year_2002 = 2002 % 4    # Not divisible by 4
year_1200 = 1200 % 400  # Divisible by 400
print("These are not leap years, determined by using the modulo operator.")
print("the year 1800 =", year_1800)
print("The year 1900 =", year_1900)
print("The year 1903 =", year_1903)
print("The year 2002 =", year_2002)
print("This is a leap year because it is divisible by 400 using the modulo operator.")
print("The year 1200 =", year_1200)
