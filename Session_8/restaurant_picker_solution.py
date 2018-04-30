#!/usr/bin/env python

import csv

restaurants = {}


def show_menu():
    print('*** MENU ***')
    print('1: Search based on distance')
    print('2: Search based on star rating')
    print('3: Add a new entry')
    print('4: Exit\n')


def search_on_distance(max_distance):
    print('\n*** DISTANCE RESULTS ***')

    for restaurant_name in restaurants.keys():
        restaurant = restaurants[restaurant_name]

        if int(restaurant['distance']) <= int(max_distance):
            print(restaurant_name)


def search_on_rating(min_stars):
    print('\n*** RATING RESULTS ***')

    for restaurant_name in restaurants.keys():
        restaurant = restaurants[restaurant_name]

        if int(restaurant['star_rating']) >= int(min_stars):
            print(
                restaurant_name + ' is a ' + restaurant['star_rating'] +
                '/5 rated place ' + str(restaurant['distance']) +
                ' minutes from here')


def add_restaurant():
    name = input('Enter Restaurant Name: ')
    cuisine = input('Enter Restaurant cuisine: ')
    cost = input('Enter Restaurant cost (out of 5): ')
    star_rating = input('Enter star rating (out of 5): ')
    distance = input('Enter distance (minutes\' walk): ')

    restaurants[name] = {
        'cuisine': cuisine,
        'cost': cost,
        'star_rating': star_rating,
        'distance': distance
    }


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
        search_on_rating(input('Please enter minimum stars: '))
        print('\n')
    elif choice == '3':
        add_restaurant()
        save_changes()
        print('\n')
    elif choice == '4':
        keep_going = False
    else:
        print('That\'s not a valid choice - try again!')
