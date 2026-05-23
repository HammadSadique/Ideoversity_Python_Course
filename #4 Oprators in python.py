# Assignment operator


a = 23
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

# Comperison Operator

a = 20
b = 30

print(a > b)
print(a < b)
print(a == b)
print(a <= b)
print(a >= b)
print(a != b)

# Assignment Operator 

a = 50
b = 20

a += b # a = a + b
print(a)

a -= b # a = a - b
print(a)
a *= b # a = a * b
print(a)

a /= b # a = a / b
print(a)

a //= b # a = a // b
print(a)

a **= b # a = a ** b 
print(a)

a %= b # a =  a % b
print(a)


# Logical Operator

a = 10
b = 5

print(a > 5 and b < 10 )
print(a > 5 or b < 10)
print(not(a < b))

# Practical Examples

age = 20
print(age >= 18)


# Using comparison operator
can_drive = age >= 18
print("Can drive:", can_drive)

# Using logical operator 'or'
# If AT LEAST ONE is True, the condition is True
is_student = True
has_coupon = False

if is_student or has_coupon:
    print("You get a discount!")
else:
    print("You pay full price.")

# Check if a number is even
num = 10
if num % 2 == 0:
    print("Is even:", num)
else:
    print("Is odd")

# Check if a character is an alphabet
score = 60
has_attendence = True
if score >= 60 and has_attendence:
    print("You are Passed")
else:
    print("You are Failed")

# --- LEAP YEAR CODE ---
year = 2024

# A year is a leap year if it is divisible by 4, but not by 100 (unless it's also divisible by 400)
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if is_leap_year:
    print(year, "is a Leap Year!")
else:
    print(year, "is NOT a Leap Year.")

is_sunny=True
is_hw_finished=True

if is_sunny==True and is_hw_finished==True:
    print("You can go outside and play!")
else:
    print("You need to finish your homework first.")


dinner_item="ice cream"

if dinner_item == "cake" or dinner_item == "ice cream":
    print("You can have dessert!")


grade="A"
percentage=89

# Agar Apka Grade A and percentage >90 then Congratlation Else: Good

if grade=="A" and percentage >90:
    print("Congratulations! You did great!")
else:
    print("Good job! Keep up the good work!")



# Not Operator

is_light_on=True

#  Not True = False
#  Not False = True
if not is_light_on:
    print("Good you are saving electricity")
else:
    print("The light is on")

province="balochistan"

# Negate 
if province != "punjab":
    print("You are eligible to vote")    

# 1) A student is allowed to sit in the exam if attendance is above 75% AND assignment is submitted.
# 2) You can go out if it’s Saturday OR Sunday, and NOT raining.

# Using Logical Operators   

is_raining=False
day_of_week="Saturday"

if (day_of_week=="Saturday" or day_of_week=="Sunday") and (not is_raining):
    print("You can go out and enjoy the day!")