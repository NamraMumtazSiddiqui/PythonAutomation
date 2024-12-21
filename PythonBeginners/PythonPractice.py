#Taking input from the User
name=input("What is your name? ")
print("Hello" +name)

#Type conversion
first_number=input("Enter first number ")
second_number=input("Enter second number ")
sum=int(first_number)+int(second_number)
print(sum)

#basicfunctions
course="Python for Beginners"
print(course.upper())
print(course.lower())
print(course.find('y')) # Python = 012345 so y is equal to 1
print(course.replace('for' ,'4'))
print('Python' in course)

#Arithmetic Functions
x=10
x=x+3
x+=3
print(x)
x*=3
print(x)

price=5
print(price < 4 or price >3)
print(not price > 4)

#If else condition
temperature=25
if temperature>30:
    print("Its a very Hot Day")
    print("Drink Plenty of Cold Water")
elif temperature>22:
    print("Its a Nice Day")
else:
    print("It is Done")

#If else another excercise with conversions and use input

weight= int(input("WHAT is your Weight"))
unit=input("Do you want to check in Kg(s) or Lb(s): ")

if unit.upper()=='K':
    converted_weightL=weight/0.45
    print("Weight in Lb(s) is" + str(converted_weightL))

else:
    converted_weightK=weight*0.45
    print("Weight in Kg(s) is" + str(converted_weightK))

 #While loop
i=1
while i<=10:
    print(i*"*")
    i=i+1

# Initialize the starting number of asterisks
j = 10

# Loop to print the reversed pattern
while j > 0:
    print('*' * j)
    j=j-1

#Lists or Array
names=["Namra" , "Mumtaz" , "Siddiqui"]
print(names[0])
print(names[-2])
print(names[0:3])
names.insert(3,"NMS")
print(names)
names.remove("NMS")
names.clear()

#for loop
for items in names :
    print(items)
#same output using for loop

k=0
while k<len(names):
    print(names[i])
    k=k+1

#range function
numbers=range(5,10)
for number in numbers:
    print(number)