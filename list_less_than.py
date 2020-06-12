a = []
b = [] 
exFlag = True

def inputException():
    print("Try again, nerd!")
 
def listAppend():
    exFlag = True
    while exFlag == True:
        try:
            listAppendNum = int(input("\nWhat number would you like to append to the list?\n"))
            exFlag = False
        except:
            inputException()
    
    a.append(listAppendNum)
    print(f"\n{listAppendNum} appended to the list.")
    input("Press any key to continue...\n")

def listIterate():
    exFlag = True
    while exFlag == True:
        try:
            listIterateNum = int(input("\nWhat number would you like to be the iteration key?\n"))
            exFlag = False
        except:
            inputException()
    if a == []:
        print("\nThe list is empty! Add numbers to the list before trying again.\n")
        input("Press any key to continue...\n")
        return
    for num in a:
        if  num < listIterateNum:
            b.append(num)
    print(f"The numbers in the list less than {listIterateNum} are: {b}")
    input("Press any key to continue, or ctrl-c to exit...\n")



while exFlag == True:
    initIn = input("\n\nWould you like to append to the list? Or iterate it?\nA. Append\nB. Iterate\n")
    if initIn == 'A' or initIn == 'a':
        listAppend()
    elif initIn == "B" or initIn == "b":
        listIterate()
    else:
        inputException()


