# compare variables and list id's when changing values.

my_age = 42.5
print(my_age)
print(id(my_age))
print(type(my_age))
# my_age id changes when you change the value.

number_apples = []
print(id(number_apples))
print(type(number_apples))
number_apples.append(300)
print(id(number_apples))
print(type(number_apples))
print(number_apples)
# number_apples id does not change when you change the value.
