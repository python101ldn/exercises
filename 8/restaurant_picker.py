#!/usr/bin/env python

# Do not edit - we need this import :)
import csv

# Do not edit - the dictionary should be empty to begin with!
restaurants = {}
# During execution it will become a dictionary containing dictionaries
# An example is below:
#
# restaurants = {
#     'Byron': {
#          'cuisine': 'burger',
#          'cost': 3,
#          'star_rating': 3,
#          'distance': 5
#      }, ...etc
# }


# Do not edit
def show_menu():
    print('*** MENU ***')
    print('1: Search based on distance')
    print('2: Search based on star rating')
    print('3: Add a new entry')
    print('4: Exit\n')


# TODO
def search_on_distance(max_distance):
    print('\n*** DISTANCE RESULTS ***')
    # 1. Loop over the restaurants dict
    # 2. Compare the distance of each restaurant to max_distance


# TODO
def search_on_rating(min_stars):
    print('\n*** RATING RESULTS ***')
    # 1. Loop over the restaurants dict
    # 2. Compare the star_rating of each restaurant to min_stars


# TODO
def add_restaurant():
    # 1. Create variables for each value you need from the user
    # 2. Use those variables fill in the below, which adds your
    # values to the restaurants dictionary on line 5

    restaurants['your variable for the name goes here'] = {
        'cuisine': 'your variable for cuisine goes here!',
        'cost': 'your variable for cost goes here!',
        'star_rating': 'your variable for star_rating goes here!',
        'distance': 'your variable for distance goes here!'
    }


# Do not edit
def save_changes():
    with open('restaurants.csv', 'w') as csvfile:
        csv_writer = csv.DictWriter(
            csvfile,
            fieldnames=['name', 'cuisine', 'cost', 'star_rating', 'distance'])
        csv_writer.writeheader()

        for restaurant_name in restaurants.keys():
            rest_details = restaurants[restaurant_name]
            rest_details['name'] = restaurant_name
            csv_writer.writerow(rest_details)


# Do not edit
def read_csvfile():
    with open('restaurants.csv', 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for rest_details in csv_reader:
            restaurant_name = rest_details['name']
            restaurants[restaurant_name] = rest_details


# Execution starts from here
read_csvfile()
keep_going = True

while keep_going:
    show_menu()
    choice = input('Please enter choice: ')
    if choice == '1':
        distance = input('Please enter max distance: ')
        search_on_distance(distance)
        print('\n')
    elif choice == '2':
        # TODO - Call the function search_on_rating
        print('\n')
    elif choice == '3':
        # TODO - Call the function add_restaurant
        # TODO - Call the function save_changes
        print('\n')
    elif choice == '4':
        # TODO - How do we prevent an infinite while loop?
        print('\n')
    else:
        print('That\'s not a valid choice - try again!')
        print('\n')
