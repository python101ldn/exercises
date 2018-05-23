random_numbers = [-1, 5.36, 0, -25, 535, -42.3]

index = 0
negatives = []

while index < len(random_numbers):
    if random_numbers[index] < 0:
        negatives.append(random_numbers[index])
    index = index + 1

print(negatives)
