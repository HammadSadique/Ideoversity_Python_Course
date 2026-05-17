
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

