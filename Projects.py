#Write a program prime number ?
'''1)My Own program  Instraction in 
If n is less than or equal to 1, it's not a prime number, so the function returns False.
If n is 2 or 3, it's a prime number, so the function returns True.
If n is divisible by 2 or 3, it's not a prime number, so the function returns False.
It checks divisibility for numbers of the form 6k ± 1 up to the square root of n. 
This optimization helps reduce the number 
of divisions needed to determine primality.
Finally, the program prompts the user to enter a number, checks if it's prime using 
the is_prime function, and prints the result.'''

while True:
    n=int(input("enter the number:"))

    if n<=1:
        print("Is not a prime number")
    elif n==2 or n==3:
        print("its a prime numbers")
    elif n%2==0 or n%3==0:
        print("is the  not prime number:")
    elif n%3!=0:
        print("is a prime number")
'''
Write a program that takes an input score from a user and prints out the corresponding letter grade 
using the following grading scale

90-100: A
80-89: B
70-79: C
60-69: D
Below 60: F
using nested if
if condition:
      print()
      if condition:
          print()
#MY Own Program     
Student=int(input("enter your Marks:"))
if Student<=100:
    Student=int(input("enter your Marks:"))
    if Student>=90:
        print("A")
    elif Student>=80:
        print("B")
    elif Student>=70:
        print("C")
    elif Student>=60:
        print("D")
    elif Student<=59:
        print("Fail")'''

 


