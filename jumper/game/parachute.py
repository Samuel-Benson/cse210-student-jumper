class Parachute():

    def __init__(self):
        self.chute = ["  ___  "," /___\\ "," \\   / ","  \\ /","   0   ","  /|\\   ","  / \\   ","^^^^^^^"]
        print(self.chute[0])
        print(self.chute[1])
        print(self.chute[2])
        print(self.chute[3])
        print(self.chute[4])
        print(self.chute[5])
        print(self.chute[6])
        print(self.chute[7])
        # Change these print statements into a parachute attribute. (a list)
        return

    def cut(self):
        # makes parachute lose one piece at top
        # SPECIAL CASE: When the last parachute piece is cut, change the stick man's
        # head from a zero ( "   0   " ) to an x ( "   x   " )
        self.chute[0] = ""
        if self.chute[0] == "":
            self.chute[1] = ""
        elif self.chute[0] and self.chute [1] == "":
            self.chute[2] = ""
        elif self.chute[0] and self.chute [1] and self.chute[2] == "":
            self.chute[3] = ""
        pass

    def is_game_over(self):
        # Return true if the parachute is dead, false it is is not
        pass

    def generate_output(self):
        # return a string of the parachute to be printed
        pass