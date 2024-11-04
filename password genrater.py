import random
print("welcom in password generator")
def end():
    return
def gernate():
    try:
        lenth=int(input("Enter the lenth of password : "))
        if 4<lenth<150:
            print("Your password is:")
        else:
            print("Pleas enter the number between 4 to 150 :")
            gernate()
    except:
        print("Invalid input!")
        gernate()
    choice=['8', 'z', '/', 'D', '#', 'L', '8', 's', '7', 'C', 'R', '3', '0', 'G', 'm', '6', '6', '%', '8', 'v', '3',
             'I', '*', 'F', '*', '@', 'h', '7', '9', '$', '0', '2', "'", '|', '(', 'n', 'X', 'y', 'w', 'd', '!', '1',
               '`', ':', '%', '7', 'H', 'g', '(', 'q', '5', '7', '"', '4', '!', 'O', 'k', '-', 'l', 'r', '}',
                 'f', 'N', '&', '0', '4', ')', '1', ')', '"', 'A', 'T', '1', '_', 't', 'E', 'a', '9', 'W', '{', 'e',
                   '[', '#', 'V', '<', 'j', '&', "'", '$', 'Y', '0', '6', 'K', '1', '2', 'u', ']', 'Q', '3', '>', '4',
                     '3', 'M', ',', '5', '9', '^', 'b', '.', '6', '2', '~', '8', 'i', 'x', '5', 'B', '2', ';', 'c', 'p',
                       '=', 'J', 'Z', '5', '4', 'U', '9', '?', 'o', 'S', '+', 'P']
    random.shuffle(choice)
    print("".join(choice[0:lenth]))
    replay_f()
def replay_f():
    replay=input("Do you want to genrate another password (yes/no)").lower()
    if replay =="yes":
        gernate()
    elif replay=="no":
        end()
    else:
        print("Invalid input!")
        replay_f()
        return

gernate()