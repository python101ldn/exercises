# Count how many words are longer than 3 letters

words = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit', 'Fusce', 'condimentum', 'quam', 'sit', 'amet', 'consequat', 'ornare', 'Maecenas', 'luctus', 'pulvinar', 'tortor', 'sit']

result = 0

for word in words:
	if len(word) > 3:
		result = result + 1

print('There are ' + str(result) + ' words more than 3 letters long')
