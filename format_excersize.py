# Four exercises to practise the format method.
print()

name = 'Phillip'
age = 42
print('{} is {}'.format(name, age))

print()

# Paragraph using quote symbols.
paragraph = '''"Python is a great language!", said
Fred. "I don't ever remember having
this much fun before."'''
print(paragraph)

print()

# Print unicode greek characters using
print("\N{GREEK CAPITAL LETTER OMEGA}")
print("\u03A9")

print()

# prints variable, item, cost (with comma separator) with 10 spaces before item and cost.
# In addition to instructions, I added the dollar sign, and float forcing 2 decimal places.
# I could have just used the dollar sign but wanted to use unicode.
item = 'car'
cost = 13499.99
space = ' ' * 10
print(space, item, space, "\u0024"'{:,.2f}'.format(cost))


