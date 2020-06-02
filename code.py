import random        
roll=input("Enter y to roll the dice: ")
while roll=="y":
    i=random.randint(1,6)
    if i==1:
        print("...........")
        print(".         .")
        print(".    0    .")
        print(".         .")
        print("...........")
    if i==2:
        print("...........")
        print(".         .")
        print(". 0     0 .")
        print(".         .")
        print("...........")
    if i==3:
        print("...........")
        print(".    0    .")
        print(".    0    .")
        print(".    0    .")
        print("...........")
    if i==4:
        print("...........")
        print(". 0     0 .")
        print(".         .")
        print(". 0     0 .")
        print("...........")
    if i==5:
        print("...........")
        print(". 0     0 .")
        print(".    0    .")
        print(". 0     0 .")
        print("...........")
    if i==6:
        print("...........")
        print(". 0     0 .")
        print(". 0     0 .")
        print(". 0     0 .")
        print("...........")    

    roll=input( "enter y to roll again: ")
