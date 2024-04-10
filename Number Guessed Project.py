#Number Guessed Project 
import random
Number= random.randint(1,20)
attempts_are=0
while True:
    Guessed_number=int(input("Please Guess my number:"))
    if Guessed_number>Number:
        print(" try again your Guessed number is big camppare to my number: ")
    elif Guessed_number<Number:
        print("Try again your Guessed Number is Small compare to my number:")
    #elif Guessed_number!=Number:
        #print("sorry your guessed number is Decimal:")
    elif Guessed_number == Number:
        print(f"It True ,number of attempts are {attempts_are}: ")
        break
        
    attempts_are=attempts_are+1
