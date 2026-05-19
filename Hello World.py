"""
Basic Python Practice Program

Description:
This beginner-friendly Python file demonstrates the use of print statements,
basic arithmetic operators, variable assignment, percentage calculation,
and triangle area calculation.

Topics covered:
- Displaying output with print()
- Addition, subtraction, multiplication, division
- Exponent and modulus operators
- Storing values in variables
- Calculating percentage
- Calculating the area of a triangle
"""

# Print function is used to display output on the terminal
print("Hello World")
print("My name is Hammad")

# Basic arithmetic operations
print(5 + 2)     # Addition
print(5 - 2)     # Subtraction
print(5 * 2)     # Multiplication
print(10 / 2)    # Division
print(5 ** 2)    # Exponent
print(10 % 2)    # Modulus
print(7 - 4 / 2) # Operator precedence example

# Variable example
age = 21
print(age)

name = "Hammad"
print(type(name))

a = 5 
print(type(a))

a = 34.55
print(type(a))

a = True
print(type(a))

a = "ha" * 5
print(a)

a = "Hello"
b = "world"
print(a +" "+ b)

# Percentage calculation
obtained_marks = 952
total_marks = 1100

percentage = (obtained_marks / total_marks) * 100
print("Percentage =", percentage)

# Triangle area calculation
base = 10
height = 20

area = (base * height) / 2

print("Area of Triangle =", area)