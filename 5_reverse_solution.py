# Reverse text provided by the user

print("Please write anything you'd like to be reversed")
user_text = raw_input()

reversed = ''

for letter in user_text:
	reversed = letter + reversed

print(reversed)