# Reverse text provided by the user

print("Please write anything you'd like to be reversed")
user_text = input()

reversed = ''

for letter in user_text:
    reversed = letter + reversed

print(reversed)

# another solution, more advanced :)
# If this is confusing try printing:
# for i in range(5, -1, -1):
#     print(i)
for position in range(len(user_text) - 1, -1, -1):
    # The end="" bit prevents the print() from ending the line each time
    print(user_text[position], end="")
print()
