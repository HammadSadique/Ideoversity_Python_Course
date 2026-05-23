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

