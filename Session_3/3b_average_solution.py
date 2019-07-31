# Write a program to find the average of a list of numbers

random_numbers = [31, 5.36, 0, 25, 535, 42.3]
total = sum(random_numbers)
average = total / len(random_numbers)

# Bit fancy - round to 2 decimal places and print
# The 0 refers to the 0th (i.e. first) variable supplied
print("{0:.2f}".format(average))
