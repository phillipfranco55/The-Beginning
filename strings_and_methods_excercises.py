

# Was asked to create a string, school with the name of my elementary school.
# Examine the methods that are available on that string. Use the help function.
# So I viewed the methods with the dir function, picked the first on the list and
# .casefold() lists all the methods with there help() file.
school = 'Jackson'
print(dir(school))
print(help(''.casefold()))

print()

country = 'usa'
correct_country = country.upper()
print(correct_country)

print()

filename = 'hello.py'
print(filename.endswith('.java'))
print(filename.index('.py'))
print(filename.endswith('world'))

print(type(school))
