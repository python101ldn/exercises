# Bob is a lackadaisical teenager.
# In conversation, his responses are very limited.
#
# Bob answers 'Hey.' if you say 'hello' to him.
# He answers 'Fine' if you say 'How are you?' or 'You good?' to him.
# He answers 'Whatever.' to anything else.

to_bob = input('What would you like to say to Bob?\n')

if to_bob == 'hello':
    print('Hey.')
elif to_bob == 'How are you?' or to_bob == 'You good?':
    print('Fine')
else:
    print('Whatever.')
