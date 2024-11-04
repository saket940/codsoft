import random
r=0
c=0
u=0
print("\nWelcome to Rock-Paper-Scissors!")
def replay(r,c,u) :
    print("Enter 'rock', 'paper', or 'scissors' to play.")
    user=input("Enter your choice (rock/paper/scissors)-").lower()
    if user not in ["rock", "paper", "scissors"]:
        print("\nInvalid choice. Please enter rock, paper, or scissors.\n")
        replay(r,c,u)
    
    computer=random.choice(['rock', 'paper', 'scissors'])
    if user == 'rock':
       don(r,c,u,user,computer)
    elif user == 'paper':
       don(r,c,u,user,computer)
    elif user == 'scissors':
       don(r,c,u,user,computer)
def winer(user, computer):
    if user == computer:
        print("tie")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("user win")
        return "u"
    else:
        print("computer win")
        return "c"        

def eror():
    print("Invalid input!")
    agan=input("Enter 'yes' for play next round and 'no' for exit-").lower()
    if agan=='yes':
        print("\nScores after",r,"rounds:")
        print("User: ",u," | Computer: ",c)
        replay(r,c,u)
    elif agan == 'no':
        print("\nThank you for playing Final Scores after-",r)
        print("User: ",u," | Computer: ",c)
        print("\nThank you for playing.")
        return
    else:
        eror()
def don(r,c,u,user,computer):
        r+=1
        a=winer(user,computer)
        if a=="c":
            c+=1
        elif a=="u":
            u+=1
        agan=input("Enter 'yes' for play next round and 'no' for exit-").lower()
        if agan=='yes':
            print("\nScores after",r,"rounds:")
            print("User: ",u," | Computer: ",c)
            replay(r,c,u)
        elif agan == 'no':
            print("\nThank you for playing! Final Scores after-",r)
            print("User: ",u," | Computer: ",c)
            print("\nThank you for playing.")
        else:
            eror()
replay(r,c,u)
