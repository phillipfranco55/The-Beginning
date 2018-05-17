# Given examples to test.

print("")
longer = """This string has
multiple lines
in it"""
print(longer)

print("")
escaped = 'I ain\'t gonna'
print(escaped)

print('')
unicode_snake = "I love \N{SNAKE}"
unicode_snake_r = r'I love \N{SNAKE}'  # Testing r with snake.
print(unicode_snake)
print(unicode_snake_r, '\n')

print('This\'s my test I ain\'t gonna lie.\n')  # I can use \n instead of print('') from now on.
print("testing \nThis \nNewline\n")  # the \n has to be next to the new word/number or it will indent.

# testing raw strings, there is no escaping.
slash_t = r'\tText \\'
print(slash_t, '\n')

normal = '\tText \\'
print(normal)

print("I ain't gonna do it!\n")


# Testing multi line triple quotes.
paragraph = """ Lorem ipsum dolor 
... sit amet, consectetur adipisicing 
... elit, sed do eiusmod tempor incididunt 
... ut labore et dolore magna aliqua. Ut 
... enimad minim veniam, quis nostrud 
... exercitation ullamco laboris nisi ut 
... aliquip ex ea commodo consequat. Duis 
... aute irure dolor in reprehenderit in 
... voluptate velit esse cillum dolore eu 
... fugiat nulla pariatur. Excepteur sint 
... occaecat cupidatat non proident,"""
print(paragraph)
