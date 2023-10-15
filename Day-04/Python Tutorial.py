# Full Python Tutorial - Day #3

# https://youtu.be/vLqTf2b6GZw?si=X6ea60CFE7Yg65Vh


#print Hello World
print("Hello World!")

#variables
a=5
print(a)

#Keyword: Already defined words

#input
name = input("What is your name? ")

#type convertion
first = input("Enter 1st number: ")
second = input("Enter 2nd number: ")

sum = int(first) + int(second)
print(sum)

#string
name= "Tony Stark"
print(name.upper())
print(name)

name= "Tony Stark"
print(name.find('S'))

name= "Tony Stark"
print(name.replace("Stark", "Iron-man"))

#operators => +,-,*,/
print(5+2)  #Add

print(5-2)  #Substract

print(5*3)  #multipy

print(5//2) #quotient

print(5%2)  #remainder

print(5**2) #power

#Shortcut
i=5
i=i+2  #can be written as i+=2

#comparision operators => True, False
print(3>2)  #--> True

print(2>3)  #--> False

print(3==2)

print(3!=2)

#Logical Operators => or, and, not
print (2>3 or 3>2)

#Conditional Statement => if/else
age=19
if(age >= 18):
    print("Adult")
else:
    print("Minor")
    
#Simple Calculator -
first = input("Enter the first number: ")
operator = input("Enter the operator (+,-,*,/,%): ")
second = input("Enter the second number: ")
first=int(first)
second=int(second)

if operator == '+':
    print(first + second)
elif operator == '-':
    print(first - second)
elif operator == '*':
    print(first * second)
elif operator == '/':
    print(first / second)
elif operator == '%':
    print(first % second)
else:
    print("Provide valid operation")

#Range-
number = range(5)
print(number)

#Loops-
i =1
while(i<=10000):
    print(i)
    i+=1

#Star pattern
i =1
while(i<=5):
    print(i*'*')
    i+=1

i =5
while(i>=0):
    print(i*'*')
    i-=1

#for with range
for i in range(5):
    print(i)

#List
marks=[95,50,60]
print(marks)

print(marks[0])
print(marks[-1])

print(marks[0:2])

for i in marks:
    print(i)

marks.append(99)
print(marks)

marks.insert(0,55)
print(marks)

print(55 in marks)

print(len(marks))

i=0
while i<len(marks):
    print(marks[i])
    i+=1

marks.clear()
print(marks)

#break and continue keyword
students=['ram','sham','atharv','yash']
for student in students:
    if student == 'sham':    #<-- stop when 'sham' ocuurs
        break
    print(student)

students=['ram','sham','atharv','yash']
for student in students:
    if student == 'sham':    #<-- exclude 'sham'
        continue
    print(student)

#Tuple : Immutable

marks=(95,98,96,55,55)

print(marks[2])
print(marks.count(95))
print(marks.index(95))

#Sets
marks={95,98,96,55,55}
#no indexing, sets are unordered

#Dictionary
marks={"Eng":95, "chem":98, "math":55}
print(marks["Eng"])

marks["phy"]= 95
print(marks)


#Functions: 1. In-build function - int(), bool()
#           2. Module funtion - import math
from math import *   #<-- import all math modules
print(sqrt(6))



















