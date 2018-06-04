# Write a function that multiplies all the numbers in a list together

def get_product_of_list(num_list):
    result = 1

    for num in num_list:
        result = result * num

    return result
