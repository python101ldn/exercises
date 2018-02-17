random_numbers = [-1, 5.36, 0, -25, 535, -42.3]

index = 0
total = 0

while index < len(random_numbers):
    total = total + random_numbers[index]
    index = index + 1

print('Total sum is ' + str(total))
