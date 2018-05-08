# Print the 2, then 3, then 4 times tables. Use nested for loops so that you don't repeat code!

for table in range(2, 5):  # range(2, 5) creates the list [2, 3, 4]
    for position in range(1, 13):
        print(position * table)
    print()  # empty line to separate tables
