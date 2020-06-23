### HELP CODING HARD REEE
### Figuring out how to make a function with a while loop that includes *potentially* more than one conditional but not *necessarily* is reeeee help.
### My code probably looks super sloppy and dumb, let me know if my mind is still not object-oriented enough lol. Classes and object types still confuse me so I avoided those like the plague

def init(initType):  ### Initialization Function
    if initType == 1:
        print("\nWelcome back! ")
    startText = "Welcome to Rock, Paper, Scissors! Press J to continue... \n"
    specInput("j", startText)
    
    if initType == 1:
        reuse()

    p1name(input, reuse)
    p2name(input, reuse)

    play()

def reuse():  ### Checking for player name reuse
    reuseText = "Would you like to change your player names? (y/N)\n"
    reuseCond = specInput("yn", reuseText)
    print(reuseCond)
    if reuseCond == "y":
        return
    elif reuseCond == "n":
        play()

    

def specInput(condition, inputText):  ### Function for specific input parameters; problem child when trying to add multiple conditions
    keyInput = input(inputText)
    keyInput = keyInput.lower()
    totalCond = False
    while totalCond == False:
        keyInput = input(inputText)
        keyInput = keyInput.lower()
        for elem in condition:
            totalCond = keyInput != elem
    return keyInput

def p1name():  ### Eventual player 1 name function
    return

def play():  ### Eventual main game function
    print("you have played")


### Ending parameter functions:

def tie():
    print("Whoops! Looks like both players picked the same move. Try again!")
    end()

def p1(winningMove, losingMove):
    print(f"Player 1 wins! {winningMove.title()} wins against {losingMove.title()}!\n")
    end()

def p2(winningMove, losingMove):
    print(f"Player 2 wins! {winningMove.title()} wins against {losingMove.title()}!\n")
    end()

def end():
    replayCond = input("Would you like to play again? (y/N)\n")
    replayCond = replayCond.lower()
    while replayCond != "y" and replayCond != "n":
        replayCond = input("Would you like to play again? (y/N)\n")
        replayCond = replayCond.lower()
    
    if replayCond == "y":
        init(1)
    elif replayCond == "n":
        exit

### Code execution and main logic; will eventually be packed into functions

init(0)

player1choice = input("Player 1, choose Rock, Paper, or Scissors...\n")
player1choice = player1choice.lower()
while player1choice != "rock" and player1choice != "scissors" and player1choice != "paper":
    player1choice = input("That's not a valid move; Player 1, choose Rock, Paper, or Scissors...\n")
    player1choice = player1choice.lower()

player2choice = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNow, Player 2, choose Rock, Scissors, or Paper...\n")
player2choice = player2choice.lower()
while player2choice != "rock" and player2choice != "scissors" and player2choice != "paper":
    player2choice = input("That's not a valid move; Player 2, choose Rock, Paper, or Scissors...")
    player2choice = player2choice.lower()

#if
if player1choice == player2choice:
    tie()
if player1choice == "rock":
    if player2choice == "paper":
        p2(player2choice, player1choice)
    if player2choice == "scissors":
        p1(player1choice, player2choice)

if player1choice == "paper":
    if player2choice == "scissors":
        p2(player2choice, player1choice)
    if player2choice == "rock":
        p1(player1choice, player2choice)

if player1choice == "scissors":
    if player2choice == "rock":
        p2(player2choice, player1choice)
    if player2choice == "paper":
        p1(player1choice, player2choice)

