# Make a list of your friends names and a list of the 10 most popular names,
# check to see if your friends names are among the most popular.


friends_names = ['Jamie', 'Gilbert', 'Calvin', 'John', 'Eric', 'Ralph']
popular_names = ['James', 'John', 'Robert', 'Michael', 'William', 'David',]
print(friends_names[3])
print(friends_names[3] in popular_names)
print(friends_names in popular_names)
popular_names_set = set(popular_names)
print(popular_names_set)
print('-' * 50)


if friends_names[0] in popular_names:
    print(friends_names[0], 'is a popular name')
else:
    print(friends_names[0], 'is not a popular name.')

if friends_names[1] in popular_names:
    print(friends_names[1], 'is a popular name.')
else:
    print(friends_names[1], 'is not a popular name.')

if friends_names[3] in popular_names:
    print(friends_names[3], 'is a popular name.')
else:
    print(friends_names[3], 'is not a popular name.')

