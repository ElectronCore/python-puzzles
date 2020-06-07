from datetime import datetime

name = input("\n\nWHAT'S YO NAME BROSKI: ")
def ageF():
    lage = 0
    try:
        lage = int(input("\nWHATS YO AGE BROSEPH: "))
        if lage >= 125:
            print("\nEY YOU THINK IM DUMB, HUH?! IT IS LITERALLY IMPOSSIBLE FOR YOU TO BE THAT OLD")
            ageF()
    except:
        print("\nBRUH ENTER A NUMBER YOU SMART ALEC")
        ageF()
    return lage

def yoF():
    yo = 0
    try:
        yo = int(input("\nWHAT AGE DO YOU WANNA CHECK WHAT YEAR IT'D BE?!?!!~: "))
        if yo >= 125:
            print("\nEY YOU THINK IM DUMB, HUH?! IT IS LITERALLY IMPOSSIBLE FOR YOU TO BE THAT OLD")
            yoF()
    except:
        print("\nBRUH ENTER A NUMBER YOU SMART ALEC")
        yoF()
    return yo
age = ageF()
finAge = yoF()
currentYear = datetime.now().year
birthYear = currentYear - age
centennialYear = birthYear + finAge
if finAge == 1 and age > finAge:
    print(f"\n\n{name}, you were {finAge} year old in {centennialYear}\n")
elif finAge == 1:
    print(f"\n\n{name}, you will be {finAge} year old in {centennialYear}\n")
elif age > finAge:
    print(f"\n\n{name}, you were {finAge} years old in {centennialYear}\n")
else:
    print(f"\n\n{name}, you will be {finAge} years old in {centennialYear}\n")
