
# Elibility for casting vote using if else statement
age = 18
if age >= 18:
    print("You are eligibe for casting vote")
else:
    print("Your are not eligible for casting vote")  


obtmarks = 992
totalmarks = 1100
percentage = (obtmarks/totalmarks) * 100
print("Percentage",percentage)
if obtmarks >= 50:
    print("You got C Grade")
else:
    print("You fail Fool")    


grade = "A"
discount = 0
total_fees = 200000

if grade == "A":
    discount = 30
elif grade == "B":
    discount = 20
elif grade == "C":
    discount == 10
else:
    discount == 5

after_discount = total_fees - (totalmarks * discount / 100)
print("Your discount is: ",discount, "%")
print("Your fees after discount is: ", after_discount)

friend_age = 45
if friend_age >= 40:
    print("Reasonable")
elif friend_age >= 30:      
    print("Good")
elif friend_age >= 20:
    print("Very Good")
else:
    print("Not Good")  

province = "Punjab"

if province == "Punjab":
    print("Lincence Closed")
elif province == "Sindh":
    print("Licenece Opened")
elif province == "Balochistan":
    print("Licence Opened")
elif province == "KPK":
    print("Licence Opened")
else:
    print("Not opened")  

 
#For Loop
for i in range(2):
    print("Hammad Sadique")

for i in range(1 , 101):
    print(i)    

for i in range(5):
    print(i)

    
for i in range(5):
    name=input("Enter your name: ")
    print(name)



# Range Based
    # range start, ending, jump 49 -- 50
for i in range(10,51,5):
    print(i)    

# Make a for loop that print evennumbers from 0 to 100

for i in range(0,101,2):
    print(i)



# Nested Loops: A loop inside another loop is called a nested loop. The inner loop will be executed one time for each iteration of the outer loop.
for i in range(5):
    # i=4
    # j=0,1,2,3,4
    for j in range(5-i):
        print("*", end="")
    print()


# Type Casting: When we have to convert one data type into another data type = Type Casting

age="23"
is_buld_on="True"
# We Can't perform any math operation because it is in str
print(type(age))

# Converting to int Type
age = int(age)
is_buld_on= bool(is_buld_on)
print(type(age))
print(age-5)


age=45

print(type(age))

# Type Cast it to String
age=str(age)
print(type(age))




age=input("Enter your age: ")
print(type(age))
age=int(age)
print(type(age))

# -5<0: T
while(age<=0):
    age=input("Please enter a valid age: ")
    age=int(age)



# ==
# != T, F
for i in range(10,50,2):
    print(i)

print(age)

real_password="abcd"

user_input=input("Enter the password: ")

while user_input != real_password:
    print("Incorrect password. Please try again.")
    user_input=input("Enter the password: ")

print("Access granted. Welcome!")


# Make a while loop to print the sum of the first 10 natural numbers (1 to 10).

num = 1
sum = 0

while num <= 10:
    sum = sum + num
    num = num + 1

print("The sum of the first 10 natural numbers is:", sum)


# The loop should continue as long as the sum is less than or equal to 100.
num = 1
total = 0

while total <= 100:
    total = total + num
    print(f"Number: {num}, Current Total: {total}")
    num = num + 1


# --- PRACTICE PROBLEMS ---


# Create a guessing game where the user has to guess a secret number (e.g., 7).

secret_number = 7

for guess in range(5): # Try up to 5 times
    user_guess = int(input("Guess the number (between 1 and 10): "))
    
    if user_guess == secret_number:
        print("Congratulations! You guessed the number.")
        break # Exit the loop if correct
    else:
        print("Wrong guess!")


# Countdown Timer: Create a countdown from 5 to 1 and then print “Start!”

for i in range(5,0,-1):
    print(i)
print("Start!") 






# 1) Use a for loop to print numbers from 1 to 540.

for i in range(1,541):
    print(i)
    


# 2) Use a while loop to keep asking the user for the password until it’s correct.

    correct_password="234"
    user_password = input("Enter the password: ")
    while user_password != correct_password:
        user_password = input("Enter the password: ")

print("Access granted. Welcome!")





# For Loop Example
print("\n--- For Loop Example ---")
for i in range(5):
    print("Hello")


# While Loop Example
print("\n--- While Loop Example ---")
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1


# Loop Control Statements: break and continue
print("\n--- Loop Control (break & continue) ---")
# Break example: stop the loop when number is 5
for number in range(1, 10):
    if number == 5:
        print("Breaking the loop at:", number)
        break
    print("Number:", number)

print()

# Continue example: skip even numbers
for number in range(1, 6):
    if number % 2 == 0:
        continue  # skip the rest of the loop body for even numbers
    print("Odd number:", number)


# Nested Loops Example (Right Triangle Pattern)
print("\n--- Nested Loops Example (Right Triangle Pattern) ---")
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()  # Move to next line

    