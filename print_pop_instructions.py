# Practising pop method along with printing out the directions to use pop.

print('-' * 100)

names = ['Phillip', 'Jamie', 'Eric']
names_attrib = dir(names)
print(type(names_attrib))
print(names_attrib)

print('-' * 100)

method_names_attrib = names_attrib[-4]
print(method_names_attrib)

print('-' * 100)

# I just copy pasta the pop method under >>> help(list)
print('How to use the method pop for lists:')
print("""'pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.'""")

print('-' * 100)

print('Example:')
print(names)
print()
print('After pop method is used:')
names.pop()
print(names)

print('-' * 100)
