# Bob is a lackadaisical teenager.
# In conversation, his responses are very limited.
#
# Bob answers 'Hey.' if you say 'hello' to him.
# He answers 'Fine' if you say 'How are you?' or 'You good?' to him.
# He answers '...sup' in response to 'hi', 'hey', 'yo' or 'howdy'.
# He answers 'AAAAH' in response to any string that begins with a capital 'A'.
# He answers 'Whatever.' to anything else.

to_bob = input('What would you like to say to Bob?\n')

greetings = ['hi', 'hey', 'yo', 'howdy']

if to_bob == 'hello':
    print('Hey.')
elif to_bob == 'How are you?' or to_bob == 'You good?':
    print('Fine')
elif to_bob in greetings:
    print('...sup')
elif to_bob[0] == 'A':
    print('AAAAH')
else:
    print('Whatever.')
