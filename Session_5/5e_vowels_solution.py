# Count number of vowels in a sentence

print("Please write a sentence and then press Enter!")
user_text = input()

vowels = ['a', 'e', 'i', 'o', 'u']
total = 0

for letter in user_text:
    if letter.lower() in vowels:  # lower() converts the letter to lower case
        total = total + 1

print('There are ' + str(total) + ' vowels')
