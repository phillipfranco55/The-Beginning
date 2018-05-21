# Create a variable, name, set to your name.
# Create another variable, second_half, that
# tests whether the name would be classified
# in the second half of the alphabet? What do
# you need to compare it to?

import string

name = input('Your name: ')
first_letter = list(name[0])
second_half = list(string.ascii_uppercase[13:26:])
print(second_half)
print(first_letter)
if bool(set(first_letter).intersection(second_half)):
    print("The first letter of your name belongs in the second half of the alphabet.")
else:
    print("The first letter of your name belongs in the first half of the alphabet.")
