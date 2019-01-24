hotel = {
    'name': 'Corinthia Hotel',
    'amenities': ['Indoor pool', 'Fitness centre', 'Spa'],
    'top spots': [
        {'name': 'Trafalgar Square',
         'proximity': 300},
        {'name': 'London Eye',
         'proximity': 450},
        {'name': 'Buckingham Palace',
         'proximity': 1200}
     ]
}

hotel_name = hotel['name']
print("hotel name:", hotel_name)

number_of_amenities = len(hotel['amenities'])
print("number of amenities:", number_of_amenities)

print("All top spots:")
top_spots = hotel['top spots']
for spot in top_spots:
    print(spot['name'])

print("Top spots that are less than 500m away:")
for spot in top_spots:
    if spot['proximity'] <= 500:
        print(spot['name'])