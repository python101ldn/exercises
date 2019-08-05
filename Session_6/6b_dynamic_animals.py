# Use input() to add someone's name and their favourite animal dynamically.

faves = {
    'Alice': 'sloth',
    'Veli': 'monkey',
    'Chiara': 'platypus'
}

print(faves)

name = input('What is your name?\n')
animal = input('What is your favourite animal?\n')

faves[name] = animal
print(faves)
