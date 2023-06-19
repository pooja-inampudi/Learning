import random
number= random.randint(1,99) 
#print(number)
while True:  
    user=int(input("Enter a number between 0 and 99:")) 
    if number == user: 
        print("The guess is correct the game ends!!!!!")
        break
    elif user<number: 
        print("The number you entered is lesser number")
        
    elif user>number: 
        print("The number you entered is large")
