# Using a while loop, reverse a string

word = 'a string to be reversed'
while_result = ''
position = 0

while len(while_result) != len(word):  # Or you could use while position < len(word)
    while_result = word[position] + while_result
    position = position + 1

print("Result from while loop: " + while_result)

# Using a for loop, reverse a string

for_result = ''

for letter in word:
    for_result = letter + for_result

print("Result from for loop: " + for_result)