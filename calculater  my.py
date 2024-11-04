print("welcome")
def repet():
 try: 
    n1=int(input("\nEnter first number- "))
    print("\n Select ope:")
    print("+ : Addition")
    print("- : Subtraction")
    print("* : Multiplication")
    print("/ : Division")

    ope=input("\nEnter operater- ")
    if ope == '+':
        print("\n")
    elif ope == '-':
        print("\n")
    elif ope == '*':
        print("\n")
    elif ope == '/':
        print("\n")
    else:
        print("Invalid operater selected!")
        repet()
    n2=int(input("Enter secand number- "))
    if ope == '+':
            print("The answer is-",n1 + n2)

    elif ope == '-':
        print("The answer is-",n1 - n2)

    elif ope == '*':
         print("The answer is-",n1 * n2)

    elif ope == '/':
        if n2 != 0:
             print("The answer is-",n1 / n2)

        else:
             print("Infinite Error: Division by zero!")
    replay=input("Enter 'yes' for reuse the calculater and 'no' for exit-").lower()
    if replay =="yes":
        repet()
    else:
        print("Thankyou for using")
        end()
 except:
  print("invled input")
  repet()
def end():
    return
repet()
