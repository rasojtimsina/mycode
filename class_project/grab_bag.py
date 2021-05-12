#!/usr/bin/env python3

num1 = int(input ("Enter first number: \n"))
num2 = int(input ("Enter second number: \n"))
num3 = int(input ("Enter third number: \n"))
def max(a,b,c):
    maximum=a
    if b>a:
        maximum=b
        if c>b:
            maximum=c
        else:
            if c>a:
                max=c
        return maximum

print(f"The max of {num1},{num2},{num3} is", max(a,b,c))

