# Write a program that prints the numbers from 1 to 100, but for
# multiples of three print “Fizz” instead of the number
# and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.

current = 1
end = 100

while current <= end:
    if current % 3 == 0 and current % 5 == 0:
        print('FizzBuzz')
    elif current % 3 == 0:
        print('Fizz')
    elif current % 5 == 0:
        print('Buzz')
    else:
        print(current)
    current += 1
