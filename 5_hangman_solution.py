# Write a hangman game!

word = 'OBJURGATE'
remaining_letters = list(word)  # a list of characters
guesses = []  # an empty list
incorrect_guesses_left = 6

while len(remaining_letters) > 0 and incorrect_guesses_left > 0:
    print('The word to guess: ', end='')
    for letter in word:
        if letter in remaining_letters:
            print('_', end='')  # do not start a new line after print
        else:
            print(letter, end='')
    print()
    print('Guesses so far: ' + ', '.join(guesses))

    guess = input('Please type a letter and press Enter\n')
    first_letter = guess[0].upper()

    if first_letter.isalpha():
        if first_letter not in guesses:
            if first_letter in remaining_letters:
                print('Bingo!')
                guesses.append(first_letter)

                while first_letter in remaining_letters:
                    remaining_letters.remove(first_letter)
            else:
                incorrect_guesses_left -= 1
                print('Wrong! You have ' + str(incorrect_guesses_left) +
                      ' guesses left.')
                guesses.append(first_letter)
        else:
            print('You\'ve already guessed that!')
    else:
        print('Please only give alphabet characters')
    print()

if len(remaining_letters) == 0:
    print('You won! The word was ' + word)
else:
    print('Better luck next time, the word was: ' + word)
