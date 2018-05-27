
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
