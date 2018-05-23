# From a list of numbers, find the largest possible product

random_numbers = [-1, 5.36, 0, -25, 535, -42.3]

first_index = 0
largest = random_numbers[0] * random_numbers[1]

while first_index < len(random_numbers) - 1:
    second_index = first_index + 1

    while second_index < len(random_numbers):
        next_sum = random_numbers[first_index] * random_numbers[second_index]

        if next_sum > largest:
            largest = next_sum

        second_index = second_index + 1

    first_index = first_index + 1

print('Largest product possible is ' + str(largest))
