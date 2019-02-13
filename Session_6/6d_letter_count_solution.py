letter_count = {}
word = 'expedia'

for letter in word:
    if letter in letter_count:
        letter_count[letter] = letter_count[letter] + 1
    else:
        letter_count[letter] = 1

print(letter_count)

# alternative solution: using a default value!
for letter in word:
    letter_count[letter] = letter_count.get(letter, 0) + 1

print(letter_count)
