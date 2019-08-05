# Write a program that splits a list into two sublists of equal length, 
# removing the last element if the list has an odd number of elements.

# The logic is in a function so I can run this code multiple times!
def split_list_in_2(my_list):
    length = len(my_list)
    halfway = length // 2 # rounds the integer down
    print("first half:", my_list[:halfway])
    print("second half:", my_list[halfway:])

even = list(range(1, 11)) # generates a list between 0 (inclusive) and 10 (exclusive of 11)
split_list_in_2(even)

odd = list(range(1, 12))
split_list_in_2(odd)
