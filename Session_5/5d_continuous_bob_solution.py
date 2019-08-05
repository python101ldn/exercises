talking = True

while talking:

    to_bob = input('What would you like to say to Bob?\n')
    greetings = ['hi', 'hey', 'yo', 'howdy']

    if to_bob.lower() == 'bye':
        print('Smell ya later.')
        talking = False
    # Below from previous weeks
    elif to_bob == 'hello':
        print('Hey.')
    elif to_bob == 'How are you?' or to_bob == 'You good?':
        print('Fine')
    elif to_bob in greetings:
        print('...sup')
    elif to_bob[0] == 'A':
        print('AAAAH')
    else:
        print('Whatever.')
