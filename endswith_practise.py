# Practise with endswith method.

my_name = 'Phillip'
print(my_name.endswith('ip'))
print(my_name.endswith('hil'))

# Changes search location to the beginning of the word.
print(my_name.endswith('ip', 0, 3))
print(my_name.endswith('Phi', 0, 3))

# Practise with startswith method.
print(my_name.startswith('Phill'))
print(my_name.startswith('llip', 3, 7))
