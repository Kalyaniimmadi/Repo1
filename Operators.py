#Control statements
#1.Decision making system
#2.Iterative Statements
#3.Transfer statements
#-------------------------------------------------------------------
print("Decision Making statements")
print("if statement")
#syntax:
'''if (condition):
       Block of code
       print()'''
print()
#Example
a,b=10,60
if a<b:
    print("if block satisfied")
print()
#------------------------------------------------------------------------------------------------------------------
print("nested if statement")
a=90
b=78
if (a>=b) and (a!=b):
    print("a is big")
    if (a is 90):
        print("its True 'a' is",a)
#--------------------------------------------------------------------------------------------------------------------------
print()
print("if else statement")
#Syntax
'''if(condition):
    print()
else:
    print()'''
b=10,
c=90
if b==c:
    print("if block is True")
else:
    print("else statement is True")#correct
#-----------------------------------------------------------------------------------------------------
print()   
print("if elif and else")
a=40
b=400
if a==b:
    print("if statement is True")
elif a<b:
    print("elif is true")#correct
elif a!=b:
    print("2nd elif is True")
else:
    print("Dear user check once your conditions")
#--------------------------------------------------------------------------------------
'''Write a program that takes an input score from a user and 
prints out the corresponding letter grade using the following grading scale:

90-100: A
80-89: B
70-79: C
60-69: D
Below 60: F
#using nested if
if condition:
      print()
      if condition:
          print()'''
#program          
student_marks = int(input("Enter your marks: "))

if student_marks <= 100:
    if student_marks >= 90:
        print("Grade: A")
    else:
        if student_marks >= 80:
            print("Grade: B")
        else:
            if student_marks >= 70:
                print("Grade: C")
            else:
                if student_marks >= 60:
                    print("Grade: D")
                else:
                    if student_marks >= 0:
                        print("Fail")
                    else:
                        print("Invalid marks entered.")
else:
    print("Invalid marks entered.")


#my Own pragram
Student=int(input("enter your Marks:"))
if Student<=100:
    Student=int(input("enter your Marks:"))
    if Student>=90 and Student<100:
        print("A")
    elif Student>=80:
        print("B")
    elif Student>=70:
        print("C")
    elif Student>=60:
        print("D")
    elif Student<=59:
        print("Fail")
 
#----------------
#iterative statements
numbers=[1,2,4,5,667,7]    
for var in numbers:
    print(var)
#--------------------
print()
num1=[9,98,8,87]   
new_list=[]
for i in num1:
    new_list.append(i)
    print(new_list)
print()
#-------------------
l=[1,2,2,3,3,2,1,11,1,1]
new_li=[]
for i1 in l:
    if i1==1:
        #print(i1)
        new_li.append(i1)
        print(new_li)
#--------------        
print()
num = 0
while num < 3:
    print(num)
    num = num + 1
    num2 = 3
    while (num2 <= 5):
        print(num2)
        num2 = num2 + 1
#----------------
for x in range(10):
    if x == 5:
        print(x)  # Prints x when it equals 5
        for y in range(10):  # Define y within the loop
            if y == 7:
               print(y)  # Prints y when it equals 7
#print(x)  # This line is commented out
#----------------               
num=0               
while (num <= 5):
    #print(num)
    num = num + 1
    print(num)
lan =input("enter tour ")

l=[1,2,3]
l.append()