
# Python Lambda
# Python’s anonymous functions refer to those that have no name and can be invoked immediately or stored within a variable. These are known as lambda functions. They can take any number of arguments and only one expression. You will learn about them in depth in this portion.
# Subjects covered in anonymous function in Python:
#         Lambda
#         Lambda with filter
#         Lambda with map
#         Lambda with reduce

# syntax:
#     lambda arguments: expression
#


a=10
b=5
c=lambda a,b:a*b
print(c(a,b))


add = lambda x, y: x + y
print(add(5, 3)) # Output: 8

# find the maximum of two numbers

max_num = lambda x,y:x if x<y else y
print(max_num(55,100))


# using map
#     map syntax = (function, iterable)

n=[1,2,3,4,5,6,7,8,9,10]

mul=list(map(lambda n:n*2,n))
print(mul)
# -----------------------------------------><----------------------------------------------------
# using filter

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8]
# -----------------------------------------><----------------------------------------------------
# Using reduce
from functools import reduce

numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result)  # Output: 10

# -----------------------------------------><----------------------------------------------------

# Sort a List of Tuples by Second Element
tuples = [(1, 2), (3, 1), (5, 4), (4, 6)]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)  # Output: [(3, 1), (1, 2), (5, 4), (4, 6)]



# key benifits of using lambda function

    # lambda allows u to define in single line
    # lambda is used for map , filter , reduce keywords

# Lambda functions are powerful in situations where you need small, simple functions without the overhead of defining a full function with def.
# They('re commonly used in functional programming techniques and when you need to pass a function as an argument. '
# 'The examples above demonstrate various real-world scenarios where lambdas make code more concise and readable.)

#
# list comprehension : single line statement

# syntax :[expression for i in iterable condition]

a=[i for i in range(10) if i%2==0]
print(a)

# Dictionary comprehension

# Python code to demonstrate dictionary
# comprehension

# Lists to represent keys and values
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]

# but this line shows dict comprehension here
myDict = { k:v for (k,v) in zip(keys, values)}

# We can use below too
# myDict = dict(zip(keys, values))

print (myDict)



