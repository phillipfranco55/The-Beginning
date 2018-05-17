# Practice using the format method

print()

name = 'Matt'
print('Hello {}'.format(name))

print()

# puts what you have in the parenthesis after format into the curly brackets
print('I:{} R:{} S:{}'.format(1, 2.5, 'foo'))

print()

# Changing the value of the format method
name = 'Paul'
print('Name: {}'.format(name))
print('Name: {name}'.format(name='John'))
print('Name: {[name]}'.format({'name': 'George'}))

my_name = {'name_my': 'Phillip', 'age_my': 42}
sentence = 'My name is {name_my} and I am {age_my} years old.'.format(**my_name)
print(sentence)
