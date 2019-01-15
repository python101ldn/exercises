# Count the number of 'a's in my_string.

total = 0
my_string = 'Today is a great day!'

for letter in my_string:
    if letter == 'a':
        total = total + 1

print('"' + my_string + '" contains ' + str(total) + 'a\'s')
