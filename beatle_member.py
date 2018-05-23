

name = input("Enter name to check if you are a Beatles member: ")
# beatle = False
if (name == 'George' or
    name == 'Ringo' or
    name == 'John' or
    name == 'Paul'):
    # beatle = True
    print("You are a Beatles member.")
else:
    # beatle = False
    print("You are not a Beatles member.")

my_name = input('Enter your real name to check to see if you are a Beatles member: ')
beatles = ['George', 'Ringo', 'John', 'Paul']
if my_name in beatles:
    print('You really are a Beatle!')
else:
    print('I knew you where not a beatle!')
