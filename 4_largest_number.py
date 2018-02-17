random_numbers = [-1, 5.36, 0, -25, 535, -42.3]

index = 1
largest = random_numbers[0]

while index < len(random_numbers):
    if random_numbers[index] > largest:
        largest = random_numbers[index]
    index = index + 1

print('Largest number of list is ' + str(largest))
