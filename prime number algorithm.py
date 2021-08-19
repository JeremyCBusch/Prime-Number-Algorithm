"""
This program is meant to prompt the user for a number and this algorithm will find every prime number from 1 to the number that the user inputs.
This is found by running through each number from 1 to N and checking if it is divisible to any number from 1 to a square root of N. If it is divisible 
to any number then if is added to a list of non prime numbers. Once every number is gone through then it will add every number that is not in the list.
The list is then returned to the user.
"""


import math


length_of_list = 0
while length_of_list < 2:
    length_of_list = int(input("This program will find all the prime numbers at or below N. Select that N: "))

assert length_of_list > 1, "length of list needs to be 2 or greater"

numbers_list = [] # this wioll be the list that will contain all numbers until N
number_into_list = 1 # this is the number to be appended into the list

# this is the loop to create a list of numbers from 1 to N 
while number_into_list <= length_of_list:
    numbers_list.append(number_into_list)
    number_into_list += 1


non_prime_numbers = [] # All non prime numbers are copied into this list
multiples = 2 # everything is a multiple of 1 so need to skip that one
index = 2 # # Changes the number to determine if it is divisible to "multiples", make sure we start with the number 3 in the list
while multiples <= math.sqrt(length_of_list):
    index = 3
    while index < length_of_list:
        if numbers_list[index]  % multiples == 0: # this if statements determines if a number is divisible to "multiples"
            non_prime_numbers.append(numbers_list[index]) 
        index += 1 
    multiples += 1

prime_numbers = [] # All non prime numbers are extracted from the "numbers_list", the remaining numbers from the list will be added to this list
for number in numbers_list:
    if non_prime_numbers.count(number) == 0 and number != 1:
        prime_numbers.append(number)

print(f'The prime numbers at or below {length_of_list} are {prime_numbers}')
