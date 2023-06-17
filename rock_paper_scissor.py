import random
user_score=0
computer_score=0
for i in range(10):
    print("round",i+1)
    options=('r','p','s')
    computer =random.choice(options)
    user=input('select one from r,p,s:')
    while  user not in options:
        user=input('select one from r,p,s:')

    print(f"user:{user}")
    print(f"computer:{computer}")
    if user == computer:
        pass
         
    elif user =="r" and computer =="p":
        computer_score+=1
    
    elif user == "r" and computer == "s":
        
        user_score+=1
    elif user == "p" and computer =="s":
        
        computer_score+=1
    elif user=="s" and computer=="r":
        
        computer_score+=1
    elif user=="p" and computer=="r":
        
        computer_score+=1
    elif user=="s" and computer=="p":
        
        user_score+=1
    print(user_score)
    print(computer_score)
if user_score> computer_score:
    print("User wins")
elif user_score==computer_score: 
    print("Tie")
else:
    print("Computer wins")

  
