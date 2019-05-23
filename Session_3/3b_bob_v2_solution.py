to_bob = input('What would you like to say to Bob?\n')

greetings = ['hi', 'hey', 'hello', 'howdy']

if to_bob.lower() in greetings:
    print('...sup')
# Below from Session 2
elif to_bob == 'hello':
    print('Hey.')
elif to_bob == 'HELLO':
    print('Woah, hey!')
elif to_bob.lower() == 'bye' or to_bob == 'goodbye':
    print('Laters.')
else:
    print('Whatever.')
