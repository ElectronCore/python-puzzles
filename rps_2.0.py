## future ideas: rewrite the game class as a standalone prototype class with arbitrary variables for everything so 
## you could change it to be a completely different game altogether. Also, maybe have the functionality to add more
## than 3 conditions; possibly use more objects to encapsulate more of the code and make it easier to read.


class RPSgame:
    
    def __init__(self):
        self.p1name = "Player 1"
        self.p2name = "Player 2"
        self.playCounter = 0
        self.types = {"r":"Rock", "p":"Paper", "s":"Scissors"}
        
    def init(self):
        if self.playCounter > 0:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome back to Rock, Paper, Scissors, friend! Press J to continue, or N to exit...\n")
        else:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome to Rock, Paper, Scissors! Press J to continue, or N to exit...\n")
        startCond = RPSgame.specInput("j", "n")
        if startCond == "n":
            exit
        elif startCond == "j":
            self.initNames()
    
    def initNames(self):
        if self.playCounter > 0:
            print("\nWould you like to use the names you have? (y/N)")
            nameReuseCond = RPSgame.specInput("y","n")
            if nameReuseCond == "y":
                self.play()
            else:  
                print("\nWhich names would you like to change? (1/2/Both)")
                whichNameChangeCond = RPSgame.specInput("1","2","both")
                if whichNameChangeCond == "1":
                    self.getName(1)
                elif whichNameChangeCond == "2":
                    self.getName(2)
                else:  
                    self.getName(1)
                    self.getName(2)
                self.initNames()
        else:
            self.getName(1)
            self.getName(2)
            self.play()

            
    
    def getName(self, player):
        if player == 1:
            print(f"\nEnter the name for {self.p1name}:\n")
            self.p1name = input().upper()
            return
            
        else:
            print(f"\nEnter the name for {self.p2name}:\n")
            self.p2name = input().upper()
            return
            

    def play(self):
        print(f"\n\n{self.p1name}, choose Rock, Paper, or Scissors. (r/p/s)")
        p1PlayChoice = RPSgame.specInput("r","p","s")
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\nNow, {self.p2name}, choose Rock, Paper, or Scissors. (r/p/s)")
        p2PlayChoice = RPSgame.specInput("r","p","s")
        self.winConditions(p1PlayChoice, p2PlayChoice)
        self.replay()

    def replay(self):
        self.playCounter += 1
        print("\nWould you like to play again? (y/N)")
        exitCond = RPSgame.specInput("y","n")
        if exitCond == "n":
            exit()
        else:
            self.init()
    
    def winConditions(self, p1, p2):
        if p1 == p2:
            print("\nIt's a draw!")
            return
        elif p1 == "r":
            if p2 == "p":
                print(f"\n{self.p2name} wins! {self.types[p2]} beats {self.types[p1]}.")
                return
            else:
                print(f"\n{self.p1name} wins! {self.types[p1]} beats {self.types[p2]}.")
                return
        elif p1 == "p":
            if p2 == "r":
                print(f"\n{self.p1name} wins! {self.types[p1]} beats {self.types[p2]}.")
                return
            else:  
                print(f"\n{self.p2name} wins! {self.types[p2]} beats {self.types[p1]}.")
                return
        elif p1 == "s":
            if p2 == "r":
                print(f"\n{self.p1name} wins! {self.types[p1]} beats {self.types[p2]}.")
                return
            else:
                print(f"\n{self.p2name} wins! {self.types[p2]} beats {self.types[p1]}.")
                return


    @staticmethod
    def specInput(*conditions, errortxt = "\nThat's the wrong input! Try again.\n"):
        storedInput = input().lower()
        while storedInput not in conditions:
            storedInput = input(errortxt).lower()
        return storedInput

rps = RPSgame()
rps.init()