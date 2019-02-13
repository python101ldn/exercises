# Bob is a lackadaisical teenager.
# In conversation, his responses are very limited.
#
# Bob answers 'Sure.' if you ask him a question.
# He answers 'Whoa, chill out!' if you yell at him.
# He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
# He says 'Fine. Be that way!' if you don't say anything.
# He answers 'Whatever.' to anything else.

to_bob = 'howdy'

if '?' in to_bob and '!' in to_bob:
    print('Calm down, I know what I\'m doing!')
elif '?' in to_bob:
    print('Sure.')
elif '!' in to_bob:
    print('Whoa, chill out!')
elif not to_bob:  # empty String == False
    print('Fine. Be that way!')
else:
    print('Whatever.')
