# Print the lowest and highest numbers in a list
numbers = [65, 4, 9, 23, 15, 875, 3.69, 33, 12, 79, 6]

sorted_numbers = sorted(numbers)
print("Lowest:", sorted_numbers[0])
print("Highest:", sorted_numbers[len(numbers) - 1])
