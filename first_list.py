# This shows that even though you change the list. The list id does not change.

names = []
print(id(names))

names.append("Fred")
print(names)
print(id(names))
