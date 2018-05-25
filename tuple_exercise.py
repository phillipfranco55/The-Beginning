# Tuple exercise.

my_name = ('Phillip', 'Franco', 42)
people = []
gf_name = ('Jamie', 'Welch', 41)
friend_name = ('Gilbert', 'Lopez', 43)
print(people)
people.append(my_name)
print(people)
people.append(gf_name)
print(people)
people.append(friend_name)
print(people)
sort_people = sorted(people)
print(sort_people)
print(type(people))
print(type(sort_people))
print(sorted(sort_people, key=lambda x: (x[0])))
print(sorted(sort_people, key=lambda x: (x[1])))
print(sorted(sort_people, key=lambda x: (x[2])))


