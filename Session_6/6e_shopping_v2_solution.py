# Let's go shopping!
inventory = {'apples': 3, 'pears': 2, 'bananas': 0}

# Add the following functionality to your shopping program:
# i. If that item doesn't exist, let the user know.
# ii. If that item is sold out, let the user know.
# iii. Also ask the user for how many items they'd like to buy.

item_name = input('What would you like to buy?\n')

if item_name in inventory:
    if inventory[item_name] == 0:
        print('Sorry, that item has sold out!')
    else:
        how_many = input('How many ' + item_name + ' would you like to buy?\n')
        how_many = int(how_many)  # convert string to number (int = integer)
        new_total = inventory[item_name] - how_many

        # Ensures your inventory is never minus
        if new_total < 0:
            print('Sorry, we could only sell you ' + str(inventory[item_name]) + ' ' + item_name)
            inventory[item_name] = 0
        else:
            inventory[item_name] = new_total
else:
    print('Sorry, we don\'t sell those.')

print('Our stock: ')
print(inventory)
