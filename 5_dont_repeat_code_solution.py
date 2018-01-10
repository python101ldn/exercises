
# (harder) Print the 2, 3 and 4 times tables (up to 12). Don't repeat code!

for table in range(2, 5):  # range(2, 5) creates the list [2, 3, 4]
	for position in range(1, 13):
		print("{} times {} is {}".format(position, table, position * table))  # fancy string formatting
	print()  # empty line to separate tables
