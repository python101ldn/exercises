possible_sums = {}

for first_dice in range(1, 7):
    for second_dice in range(1, 7):
        dice_sum = first_dice + second_dice

        if dice_sum in possible_sums:
            possible_sums[dice_sum] = possible_sums[dice_sum] + 1
        else:
            possible_sums[dice_sum] = 1

print(possible_sums)
