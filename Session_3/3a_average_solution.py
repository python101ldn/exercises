# Write a program to find the average of a list of numbers

random_numbers = [31, 5.36, 0, 25, 535, 42.3]

# We'll find a better way to do this in week 4!
total = 0
total = total + random_numbers[0]  # 31
total = total + random_numbers[1]  # 36.36
total = total + random_numbers[2]  # 36.36
total = total + random_numbers[3]  # 61.36
total = total + random_numbers[4]  # 596.36
total = total + random_numbers[5]  # 638.66

average = total / len(random_numbers)

# Bit fancy - round to 2 decimal places and print
# The 0 refers to the 0th (i.e. first) variable supplied
print("{0:.2f}".format(average))
