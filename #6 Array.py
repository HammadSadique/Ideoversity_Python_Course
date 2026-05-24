name = ["Hammad", "Ali", "Talha"]
print(name)
print(name[0])
print(name[1])
print(name[2])
name.append("Umair")
print(name)
name.insert(1,"Zeeshan")
print(name)
name.remove("Hammad")
print(name)
name.pop(1)
print(name)
name.pop()
print(name)

name = "Hammad"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

# Make a program to add the marks of 5 students using arrays/list.
# marks = []
# for i in range(5):
#     mark = int(input("Enter mark: "))
#     marks.append(mark)
#     print(marks)
#     print(sum(marks))


# name = []   
# for i in range(5):
#     name = input("Enter a name: ")
#     name.append(name)        
# print(name)


students =["Ali", "Ahmed", "Talha", "Hammad", "Zeeshan"]
employee = ["hammad", "ali", "talha", "umair", "saif"]

name = input("Enter your Name: ")
if name in students:
    print(name , " is  a student")
elif name in employee:
    print(name , " is  an employee")
else:
    print(name , " is  not found in list")