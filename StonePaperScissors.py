import random
rock=''''

    __________
---'    ______)
       (________)
       (________)
       (_______)
---'___(______)
'''

paper=''''

    ________
---'    ____)____
            _______)
           _________)
           ______)
---'___________)
'''

scissors=''''

    ________
---'    ____)____
            ______)
        ____________)
       (_______)
---'___(______)
'''
you=0
computer=0
loop=""
options=[rock,paper,scissors]
while(loop!='stop'):
    choice=int(input("Enter your choice 0-rock 1-paper 2-Scissors: "))
    comp=random.randint(0, 2)
    if choice==comp:
        print(f"Your Option: {choice}\n")
        print(options[choice])
        print(f"Computer Option: {comp}\n")
        print(options[comp])
        print('Draw')
    elif choice==0 and comp==1:
        print(f"Your Option: {choice}\n")
        print(options[choice])
        print(f"Computer Option: {comp}\n")
        print(options[comp])
        print('Computer won')
        comp+=1
    elif choice==0 and comp==2:
        print(f"Your Option: {choice}\n")
        print(options[choice])
        print(f"Computer Option: {comp}\n")
        print(options[comp])
        print('You won')
        you+=1
    elif choice==1 and comp==0:
        print(f"Your Option: {choice}\n")
        print(options[choice])
        print(f"Computer Option: {comp}\n")
        print(options[comp])
        print('You won')
        you+=1
    elif choice==1 and comp==2:
        print(f"Your Option: {choice}\n")
        print(options[choice])
        print(f"Computer Option: {comp}\n")
        print(options[comp])
        print('Computer won')
        comp+=1
    elif choice==2 and comp==0:
        print(f"Your Option: {choice}\n")
        print(options[choice])
        print(f"Computer Option: {comp}\n")
        print(options[comp])
        print('Computer won')
        comp+=1
    elif choice==2 and comp==1:
        print(f"Your Option: {choice}\n")
        print(options[choice])
        print(f"Computer Option: {comp}\n")
        print(options[comp])
        print('You won')
        you+=1
    loop=input("type 'stop' to finish or click Enter to continue ")
print(f"\n-------SCORE-------\nYou: {you}\tComputer: {comp}\n")
if you==comp:
    print("It's a draw:-|")
elif you<comp:
    print("Computer won:-(")
else:
    print("You Won!!!:-)")