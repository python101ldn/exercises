# 1. Define a function that takes two arguments: food and number of items,
# and returns the cost of those items using the prices dictionary
# e.g. you're buying 2 oranges, this should cost £1.60 in total

prices = {
    'banana': 0.17,
    'apple': 0.32,
    'orange': 0.80,
    'pear': 0.41
}

def calculate_cost(item, number_of_items):
    if item in prices:
        return prices[item] * number_of_items
    else:
        return 0


# 2. Define a function that returns the cost for the below shopping cart

shopping_cart = {
    'banana': 3,
    'orange': 2
}

def calculate_total(cart):
    total = 0

    for item in cart.keys():
        total = total + calculate_cost(item, cart[item])

    return total


# 3. Change your existing functions to only add to the bill if the item is in stock

stock_levels = {
    'banana': 6,
    'apple': 0,
    'orange': 32,
    'pear': 15
}

def calculate_cost_with_stock_check(item, number_of_items):
    if item in prices and stock_levels[item] > 0:
        return prices[item] * number_of_items
    else:
        return 0

