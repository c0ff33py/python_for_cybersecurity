# Example of a "for" loop with the keyword and the "range()" function:

for number in range(1, 6+1, 2):
    print(number * 3)

'''The range() function
The range() function generates a sequence of numbers. code uses range(1, 6+1, 2) which simplifies to range(1,7,2).
This function takes three arguments: a strat value, a stop value and a step value.
start value: 1
stop value: 7
step value: 2
so, between 1 and 7 value must be 1, 3, 5 

it will print 3,9,5
'''

for number in range(2, 8):
    print(number ** 2)

