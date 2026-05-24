# Function Declaration & Definition

def say_hi():
    print("Hello User")
    print("Welcome to Agentic AI 2 month Course")

# Function Calling

say_hi()
say_hi()
say_hi()



def ask_age_and_check_elgibility():
    age=input("Enter your age: ")
    age=int(age)

    if age>=18: 
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

ask_age_and_check_elgibility()
ask_age_and_check_elgibility()
ask_age_and_check_elgibility()
#Make a Function to Calculate BMI (Body Mass Index)



def calculate_bmi():
    w=input("Enter your weight in kg: ")
    # TYpe Casting
    w=float(w)
    h=input("Enter your height in meters: ")
    h=float(h)
    bmi=w/(h**2)
    return bmi

bmi=calculate_bmi()

if bmi<18.5:
    print("You are underweight.")
elif bmi<25:
    print("You are normal weight.")
elif bmi<30:
    print("You are overweight.")
else:
    print("You are obese.")

# Function parameter
def check_age_eligible(age,domicile):
    if age>=18 and domicile=="Lahore":
        print("You are Eligible to vote")
    else:
        print("You are not eligible to vote.")

# Function Argument
check_age_eligible(23,"Lahore")        
check_age_eligible(17,"Karachi")
print("You are eligible for vote")        
print("You are not eligible for vote")     

# Default Parameter
def say_hello(name,greeting="Hello"):
    print(f"{greeting},{name}")

# Calling with default
say_hello("Hammad")
say_hello("Hammad","Hi")


# Return Statements

def check_age_eligibility(age,domicile):
    if age>=18 and domicile=="lahore":
        return True
    else:
        return False

isEligible=check_age_eligibility(23,"lahore")
print(isEligible)



# percentage calculator , obtMarks, totalMarks 
#  percentage return 
# Compute age from year of birth 


# Make a Function that return Percentage 
def check_percentage(obtMarks,totalMarks):
    percentage=(obtMarks/totalMarks)*100
    return percentage

percentage=check_percentage(992,1100)
print(percentage)

# Compute age from year of birth 

def compute_age(year_of_birth):
    current_year = 2026  # You can change this to the current year
    age = current_year - year_of_birth
    return age

# Example usage
yob = int(input("Enter your year of birth: "))
age = compute_age(yob)
print("You are approximately", age, "years old.")   



def triangle_area(base,height):
    area = (base * height)/2
    return area
base = float(input("Enter base: "))
height = float(input("Enter Height: "))
#Fumction Call
result = triangle_area(base, height)

print("Area of Triangle =", result)



def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False


    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")
    