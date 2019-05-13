# Bob is a lackadaisical teenager.
# In conversation, his responses are very limited.
#
# Bob answers 'Hey.' if you say 'hello' to him.
# He answers 'Woah, hey!' if you say 'HELLO' to him.
# He answers 'Laters.' if you say 'bye', 'BYE' or 'goodbye' to him.
# He answers 'Whatever.' to anything else.

to_bob = input('What would you like to say to Bob?\n')

if to_bob == 'hello':
    print('Hey.')
elif to_bob == 'HELLO':
    print('Woah, hey!')
elif to_bob.lower() == 'bye' or to_bob == 'goodbye':
    print('Laters.')
else:
    print('Whatever.')
