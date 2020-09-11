#!/usr/bin/env python3

"""
- In this file i'll be solving 10 challenging questions using
Methods and Functions in Python
- Solving these challenges demonstrate your comprehension how methods and functions work in Python
- The complexity of the problem are gradually increasing

Note
- Questions were obtained from Pierian-Data/Complete-Python-3-Bootcamp
- All solutions are my solutions to the problem. No solutions from Pierian-Data were used
"""


#Problem 1
"""
Problem: Write a function called myfunc that prints the string "Hello World"
"""
def myfunc():
    print("Hello World")
myfunc()

#Problem 2 
"""
Problem: Define a fuction called myfunc that takes in a name, and prints: 'Hello Name'
Also, do ot use f-string
"""
def myfunc1(name): #defining the functions as myfunc1 since I already have a function called myfunc in problem 1
    print('Hello ' + name)
myfunc1('Carlos')

#Problem 3
"""
Problem: Define a function called myfunc that take in a Boolean value (True or False). 
If True, return 'Hello'
If False, return 'Goodbye'
"""
def myfunc2(condition): #from this point on, it's known that the def of my function has to be different as the one pompted in the problem
    if condition == True:
        return 'Hello'
    elif condition == False:
        return 'Goodbye'
    else:
        pass
print(myfunc2(True))

#Problem 4
"""
Problem: Define a function called myfunc that takes three arguments: x,y,andz
if z is True, return x
if z is False, return y 
"""
def myfunc3(x,y,z):
    if z == True:
        return x
    elif z == False:
        return y
    else:
        pass
print(myfunc3(2,3,True))

#Problem 5
"""
Problem: Define a function called myfunc that takes in two argument and returns their sum
"""
def myfunc4(num1,num2):
    return num1+num2
print(myfunc4(1,2))

#Problem 6
"""
Problem: Define a function called is_even that takes in one argument
that it returns True if the passed-in value is even
and returns False if it's not
"""
def is_even(number):
    if number % 2 == 0: # '%' represents mod operator that returns the remainder of a division
        return True     # if the remainder is 0, the argument is event, otherwise it's not even (an odd number)
    elif number % 2 != 0:
        return False
    else:
        pass
print(is_even(4))

#Problem 7
"""
Problem: Define a function called is_greater that takes in two arguments
and it retunrs True if the first value is greater than the second
it returns False if it is less than or equal to the second
"""
def is_greater(num3,num4):
    if num3 > num4:
        return True
    elif num3 <= num4:
        return False
    else:
        pass
print(is_greater(2,3))

#Problem 8
"""
Problem: Define a function called myfunc that takes in an arbirtray number of arguments
and returns the sum of those arguments

Note: '*args' in python allows to accept abritrary number of arguments and keyword arguments without having to pre-defined a bunch of
parameters in your function calls
"""
def myfunc5(*args):
    return sum(args)
print(myfunc5(1,2,3,4,5,6,7,0,2,3,4,6,8))

#Problem 9
"""
Problem: Define a function called myfunc that takes in an arbitrary number of arguments
it returns a list containing only those arguments that are even
"""
def myfunc6(*args):
    mylist = []
    for thisnumber in args: #first you have to iterate on all the values
        if thisnumber % 2 == 0: #then you have to check if they're even or not
            mylist.append(thisnumber)
    return mylist
print(myfunc6(1,2,2,3,4,10,21,45,48,22,34,50))

#Problem 10
"""
Problem: Define a function called myfunc that takes in a string
it returns a matching string where every even letter is uppercase 
and every odd letter is lowercase
Assume that the income string only contains letters; don't worry about numbers, spaces, and punctuations
The output string can start with either an uppercase or lowercase letter, so long as letters alternate throughout the string
"""
def myfunc7(mainstring):
    outstring = '' #declaring the an empty string that will be returned
    
    for position,letter in enumerate(mainstring): #enumerate adds a counter to an iterable and returns it in a form of enumerate object
        if position % 2 == 0:
            outstring += letter.upper()
        elif position % 2 != 0:
            outstring += letter.lower()
        else:
            pass
    return outstring
print(myfunc7('AntHropOmorphism'))