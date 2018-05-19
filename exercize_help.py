

name = 'Phillip'
print(dir(name))

print()

print(help('word'.find('d')))

print()


print(help(''.title()))

print()

# Print the dir of my age in a string.
age = 42
print(dir(age))

print()

# Print the help of the .numerator method.
from fractions import Fraction  # This should be up top, i'm keeping it here to bundle it with the exercise.
a = Fraction(1, 2)
print(type(a))
print(a)
print(help(a.numerator))
print(help(Fraction(2, 3).numerator))
