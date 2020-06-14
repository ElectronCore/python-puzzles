def inputException():
    print("\nTry again, nerd!\n")

def divisors():
    evenlyDividedBy = [] 
    divisorList = range(2, dividend)
    for divisor in divisorList:
        if dividend % divisor == 0:
            evenlyDividedBy.append(divisor)
        else: pass
    
    
    print(f"{dividend} has {len(evenlyDividedBy)} divisors: {evenlyDividedBy}\n\n")


exFlag = True
while exFlag == True:
    try:
        dividend = int(input("Input a number you would like to check the divisors of:\n"))
        divisors()
    except ValueError: inputException()
    except KeyboardInterrupt: exFlag = False