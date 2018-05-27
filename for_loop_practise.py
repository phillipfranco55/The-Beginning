
line = '-' * 100

print()
my_cat = 'cat'
cat = list(my_cat)
print(cat)
print()

print()
for letter in cat:  # letter can be anything.
    print(letter)
print()

print(type(letter))

print('-' * 100)

# Is a way to find the index of a long list. But there is a better way.
animals = ['cat', 'dog', 'bird']
for index in range(len(animals)):  # again index can be anything.
    print(index, animals[index])

print()

for index, value in enumerate(animals):  # Both index and value can be anything.
    print(index, value)

print('-' * 100)

print(index)
print(value)

print('-' * 100)

numbers = [3, 5, 9, -1, 3, 1]
result = 0
for item in numbers:
    if item < 0:
        break
    result += item  # Has to be indented under if because it is part of that block. Also same as result = result + item
print(result)

print('-' * 100)

for item in numbers:
    if item < 0:
        continue
    result += item
print(result)

print('-' * 100)

names = ["John", 'Paul', 'George', 'Ringo']
names_to_remove = []
for name in names:
    if name not in ['John', 'Paul']:
        names_to_remove.append(name)
for name in names_to_remove:
    names.remove(name)
print(names)
print()
# Another way to remove names is to use slice.
beatle_names = ['John', 'Paul', 'George', 'Ringo']
for name in beatle_names[:]:  # Copy of names.
    if name not in ['John', 'Paul']:
        beatle_names.remove(name)
print(beatle_names)

print('-' * 100)

items = [1, 3, 5, 7, 9]
positive = False
for num in items:
    if num > 0:
        break
else:
    positive = True
print(positive)
print(num)

print(line)

n = 100
while n > 0:
    print(n)
    n = n - 20
print(type(n))
print(n)
list(n)
