 
def checkEven():
    flag1 = False
    while flag1 == False:
        try:
            arg1 = int(input("What number do you want to check?\n"))
            flag1 = True
        except ValueError:
            inputException()
    
    if arg1 % 2 == 0:
        print(f"\nYes, {arg1} is an even number; are you dumb?")
    else:
        print(f"\nNo you baka, {arg1} is not an even number!")
    
def checkDivisble():
    arg1 = ''
    arg2 = ''
    flag1 = False
    while flag1 == False:
        try:
            arg1 = int(input("Input dividend: \n"))
            flag1 = True
        except:
            inputException()
    
    flag2 = False
    while flag2 == False:
        try:
            arg2 = int(input("Input divisor: \n"))
            flag2 = True
        except:
            inputException()
    
    if arg1 % arg2 == 0:
        print(f"\nYes, {arg1} can be evenly divided by {arg2}.\n")
    else:
        print(f"\nNo you fool, you've killed us all. {arg1} cannot be evenly divided by {arg2}!\n")
        
def inputException():
    print("\nYou entered the wrong thing, idiot! Learn to follow instructions, baka!\n")
    return

startFlag = True
while startFlag == True:
    startSelect = input("\n\n\nWhat do you want to do?\nPress A to Check if a number is even or odd: \nPress B if a number can be evenly divisable by another:\n")
    if startSelect == 'a' or startSelect == 'A':
        checkEven()
        startFlag = False
    elif startSelect == 'b' or startSelect == 'B':
        checkDivisble()
        startFlag = False
    else:
        inputException()
