# Write code that will print out an n row high triangle. For example if the
# user enters '4', the program should print out:
#
#       *
#      ***
#     *****
#    *******

tree_height = input('Type the desired height, and press Enter\n')
tree_height = int(tree_height)  # convert to number - might fail!

current_height = 0
max_width = tree_height * 2 - 1

while current_height < tree_height:
    stars = '*' * (current_height * 2 + 1)
    spacing = ' ' * int((max_width - len(stars)) / 2)
    print(spacing + stars + spacing)
    current_height = current_height + 1
