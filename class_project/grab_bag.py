#!/usr/bin/env python3
import os
import random
print("Welcome to Grab Bag! You first grab is \n\n")

def random():
    n = int(input("Enter between 0-3: "))
    
    if n == 0:
        maximum_number()
    elif n == 1:
        reverse()
    elif n == 2:
        get_sum()
    elif n == 3:
        multiply_number()

def maximum_number(): 
    num1 = int(input ("Enter first number: \n"))
    num2 = int(input ("Enter second number: \n"))
    num3 = int(input ("Enter third number: \n"))
    def maximum(a,b,c):
        if (a >= b) and (a >= c):
            max=a
        elif (b >= a) and (b >= c):
            max = b
        else:
            max=c
        return max
    print(f"The max of {num1},{num2},{num3} is", maximum(num1,num2,num3))

def reverse():
    def my_function(x):
        return x[::-1]
    mytxt = my_function(input("Please enter the string you want to reverse: "))
    print(mytxt)

def get_sum():
    list = []
    num = int(input("How many number do you want to add?\n >"))
    for n in range(num):
        numbers = int(input("Enter the number you want to add: "))
        list.append(numbers)
    print("Sum of the list of number provided is: ", sum(list))

def multiply_number():
    num_1 = input("Enter the first number: ")
    num_2 = input("Enter the second number: ")
    product = float(num_1) * float(num_2)
    print(f"Product of {num_1} and {num_2} is {product}")

random()
