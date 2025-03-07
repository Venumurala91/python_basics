# Operators in python
#
#     Operators are the symbols or keywords that are used to perform operations on data .
#
# Types of Operators in Python
#     Arithmetic Operators
#     Comparison Operators
#     Logical Operators
#     Bitwise Operators
#     Assignment Operators
#     Identity Operators and Membership Operators


# Variables
a = 15
b = 4

# Addition
print("Addition:", a + b)

# Subtraction
print("Subtraction:", a - b)

# Multiplication
print("Multiplication:", a * b)

# Division
print("Division:", a / b)

# Floor Division
print("Floor Division:", a // b)

# Modulus
print("Modulus:", a % b)

# Exponentiation
print("Exponentiation:", a ** b)


#
# 1. Floor Division (//):
# Purpose: Performs division and returns the quotient rounded down to the nearest integer.
#
# Description: The // operator divides two numbers and returns the integer part of the result, effectively "flooring" the result (rounding down).
#
# Example:
#
# python
# Copy
# Floor Division
a = 7
b = 2
result = a // b
print(result)  # Output: 3
# In this case:
#
# 7 // 2 gives 3 because it rounds down the result (which is 3.5) to the nearest integer.
# Another example with negative numbers:
#
# python
# Copy
# Negative Numbers
a = -7
b = 2
result = a // b
print(result)  # Output: -4
# Here:

# -7 // 2 gives -4 because the result of the division (-3.5) is rounded down to the next lower integer (i.e., -4).

# 2. Float Division (/):
# Purpose: Performs division and returns the exact quotient as a floating-point number.
#
# Description: The / operator always returns a floating-point number, regardless of whether the input numbers are integers or floats.
#
# Example:

# python
# Copy
# Float Division
a = 7
b = 2
result = a / b
print(result)  # Output: 3.5
# In this case:

'''7 / 2 gives 3.5 because it returns the exact division result as a float.
Another example with negative numbers:'''''

'''python
Copy
# Negative Numbers'''
a = -7
b = 2
result = a / b
print(result)  # Output: -3.5
# Here:

# -7 / 2 gives -3.5 because it returns the exact result as a float.

'''Bitwise Operators in Python are as follows:

Bitwise NOT
Bitwise Shift
Bitwise AND
Bitwise XOR
Bitwise OR
Example of Bitwise Operators in Python:

'''

a = 10
b = 4

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)


'''Identity Operators in Python
In Python, is and is not are the identity operators both are used to check if two values are located on the same part of the memory. Two variables that are equal do not imply that they are identical. 

is          True if the operands are identical 
is not      True if the operands are not identical 


Example of Identity Operators in Python:'''



a = 10
b = 20
c = a

print(a is not b)
print(a is c)