# Get the below code to run in a while loop until the user enters 'EXIT'
# users_name = input('What is your name? ')
# print('Hello, ' + users_name + '!')

loop = True

while loop:
    users_name = input('What is your name? ')
    if users_name.upper() != 'EXIT':
        print('Hello, ' + users_name + '!')
    else:
        print('Goodbye!')
        loop = False
