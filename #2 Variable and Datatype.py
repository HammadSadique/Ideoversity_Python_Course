# Variable
x = 5
y = "John"
print(x)
print(y)


# Typecasting
# Integer
age = 18
salary = 189000
temperature_celsius = -15
bank_balance = -200

print(type(age))  # -> type function will return type of data stored in variable
print(type(salary))
print(type(temperature_celsius))
print(type(bank_balance))


# Float
percentage_marks = 96.98
price = 799.99
net_profit = -434.67

print(type(percentage_marks))
print(type(price))
print(type(net_profit))

# Complex
complex_number = 5 + 6j

print(type(complex_number))

# String
name = "Hammad"
full_name = 'Hammad Sadique'

print(type(name))
print(type(full_name))


# Length of string
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.") 

# List 
list = [8, 2.5,[3, 5, 9],[3, 4]]
print(list)
print(type(list))

tuple = (("parrot", "Sparrow", ("Lion", "Deer")))
print(tuple)
print(type(tuple))

# Dictionary (Mapped Data)

dict = {"name": "Hammad", "age": 21, "Can vote": True}
print(dict)
print(type(dict))


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

# Calculator Using Python

a = 20
b = 30

print("The value of,", a, " + ", b, " is: ", a + b)
print("The value of,", a, " - ", b, " is: ", a - b)
print("The value of,", a, " * ", b, " is: ", a * b)
print("The value of,", a, " / ", b, " is: ", a / b)
print("The value of,", a, " % ", b, " is: ", a % b)

