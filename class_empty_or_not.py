# Write code to check if class has names or not.

names = ['Phillip', 'Gilbert', 'Ralph', 'John']
print(bool(names))
if names:
    print('Class has names, they are:', ', '.join(names))
else:
    print('Class is empty')
