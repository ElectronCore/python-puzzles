### Here's a really dumb rock-paper-scissors game! With waaaaaaaaay too much functionality. Oh well!

p1name = ""
p2name = ""

def init(initType = 0):  ### Initialization function
    if initType == 1:
        print("\nWelcome back! ")
    specInput("j", txt = "Welcome to Rock, Paper, Scissors! Press J to continue... \n")
    
    if initType == 1:
        nameInit = reuse()
        names(nameInit)
        play()
    else:
        names()
        play()

def names(nameCond = "Both"): ### Player name change function
    global p1name
    global p2name
    if nameCond == "1":
        p1name = input("Choose a name for Player 1...\n")
    elif nameCond == "2":
        p2name = input("Choose a name for Player 2...\n")
    else:
        p1name = input("Choose a name for Player 1...\n")
        p2name = input("Choose a name for Player 2...\n")


def reuse():  ### Checking for player name reuse
    reuseCond = specInput("y", "n", txt = "Would you like to change your player names? (y/N)\n")
    if reuseCond == "y":
        nameInit = specInput("1", "2", "both", txt = "Which names would you like to change? (1/2/Both)\n")
        return nameInit
    else: play()

    

def specInput(*condition, txt, errortxt = None):  ### Function for specific input parameters
    if errortxt == None:
        errortxt = txt
    ioInput = input(txt)
    ioInput = ioInput.lower()
    
    while ioInput not in condition:
        ioInput = input(errortxt)
        ioInput = ioInput.lower()
        
    return ioInput

def play():  ### Main gameplay function
    p1play = specInput("rock", "paper", "scissors", txt = f"{p1name}, choose Rock, Paper, or Scissors...\n", errortxt = f"That's not a valid move; {p1name}, choose Rock, Paper, or Scissors...\n")
    p2play = specInput("rock", "paper", "scissors", txt = f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNow, {p2name}, choose Rock, Scissors, or Paper...\n", errortxt = f"That's not a valid move; {p2name}, choose Rock, Paper, or Scissors...\n")
    if p1play == p2play:
        tie()
    if p1play == "rock":
        if p2play == "paper":
            p2(p2play, p1play)
        if p2play == "scissors":
            p1(p1play, p2play)

    if p1play == "paper":
        if p2play == "scissors":
            p2(p2play, p1play)
        if p2play == "rock":
            p1(p1play, p2play)

    if p1play == "scissors":
        if p2play == "rock":
            p2(p2play, p1play)
        if p2play == "paper":
            p1(p1play, p2play)

### Ending parameter functions:

def tie():  ### A tie ending result
    print("Whoops! Looks like both players picked the same move. Try again!")
    end()

def p1(winningMove, losingMove):  ### A player 1 winning ending result
    print(f"{p1name} wins! {winningMove.title()} wins against {losingMove.title()}!\n")
    end()

def p2(winningMove, losingMove):  ### A plater 2 winning ending result
    print(f"{p2name} wins! {winningMove.title()} wins against {losingMove.title()}!\n")
    end()

def end():  ### Final replay/exit function
    replayCond = specInput("y", "n", txt = "Would you like to play again? (y/N)\n")
    
    if replayCond == "y":
        init(1)
    elif replayCond == "n":
        exit

### Initialization function call

init()
