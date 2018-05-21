# Create a variable, age, set to your age. Create another variable,
# old, that uses a condition to test whether you are older than 18.
# The value of old should be True or False.

age = input('Enter age: ')
old = 18
if int(age) > int(old):
    print("You are {} so you are old!".format(age))
else:
    print("You are only {} so you are not old.".format(age))
