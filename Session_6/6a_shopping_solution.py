# Let's go shopping!
inventory = {'apples': 3, 'pears': 2, 'bananas': 0}

# The program should:
# Ask what the shopper would like to buy, and take user input.
# Minus 1 of that item from that inventory.

item_name = input('What would you like to buy?')

# this will fail if item_name isn't in the dictionary - see 6c solution!
inventory[item_name] = inventory[item_name] - 1
print(inventory)
