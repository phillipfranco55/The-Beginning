
# if statements by default determine if something is True or False.
name = input('Enter Name: ')
if name:
    print("The name is {}".format(name))
else:
    print('Name is missing')


class Nope:
    def __bool__(self):
        return False


n = Nope()
print(bool(n))


def hello():
    print('hi')

result = hello()
print(result)

a = None
b = None
print(id(a))
print(id(b))
y = 'None1'
z = 'None1'
print(id(y))
print(id(z))
print(a is b)
print(y is z)
if a is None:
    print("A is not set!")
