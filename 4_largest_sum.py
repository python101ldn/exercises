# From a list of numbers, find the largest possible sum of two of them.

random_numbers = [-1, 5.36, 0, -25, 535, -42.3]

index = 0
largest_sum = random_numbers[0] + random_numbers[1]

while index < len(random_numbers)-1:
    next_index = index+1
    while next_index < len(random_numbers)-1:
        next_sum = random_numbers[index]+random_numbers[next_index]
        if next_sum > largest_sum:
            largest_sum = next_sum
        next_index = next_index + 1
    index = index + 1

print('Largest sum possible is ' + str(largest_sum))
