# Compare attributes of tuples and lists.

print('-' * 100)

list_names = ['Phillip', 'Jamie', 'Eric', 'Gilbert']
print(list_names)
print(type(list_names))

print()

tuple_names = ('Phillip', 'Jamie', 'Eric', 'Gilbert')
print(tuple_names)
print(type(tuple_names))

print('-' * 100)

print('Methods of list_names:')
print(dir(list_names))
print(type(list_names))

print()

print('Methods of tuple tuple_names:')
print(dir(tuple_names))
print(type(tuple_names))

print('-' * 100)

attrib_list_names = dir(list_names)
set_attrib_list_names = set(attrib_list_names)
print(type(set_attrib_list_names))

print()

attrib_tuple_names = dir(tuple_names)
set_attrib_tuple_names = set(attrib_tuple_names)
print(type(set_attrib_tuple_names))

print('-' * 100)

print('These list methods are not in a tuple:')
print(set_attrib_tuple_names ^ set_attrib_list_names)

print('-' * 100)
