# Reverse text provided by the user

print("Please write anything you'd like to be reversed")
user_text = input()

reversed = ''

for letter in user_text:
	reversed = letter + reversed

print(reversed)

# another solution, more advanced :)
for position in range(len(user_text) - 1, -1, -1):
	print(user_text[position], end="")
print()
