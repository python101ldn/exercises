random_numbers = [1, 5, 0, -2, 3, -4, -3, 11, 5]
index = 0
negatives = []

while index < len(random_numbers):
    if random_numbers[index] < 0:
        negatives.append(random_numbers[index])
    index = index + 1

print(negatives)
