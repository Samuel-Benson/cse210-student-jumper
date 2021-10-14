class Parachute():

    def __init__(self):
        self.chute = ["  ___  "," /___\\ "," \\   / ","  \\ /","   0   ","  /|\\   ","  / \\   ","^^^^^^^"]
        # Change these print statements into a parachute attribute. (a list)
        return

    def cut(self):
        # makes parachute lose one piece at top
        # SPECIAL CASE: When the last parachute piece is cut, change the stick man's
        # head from a zero ( "   0   " ) to an x ( "   x   " )
        chute.pop(0)
        if chute.pop(0) = "   0   ":
            chute[0] = "   X   "
        pass

    def is_game_over(self):
        # Return true if the parachute is dead, false it is is not
        if chute[0] = "   X   ":
            return True
        pass

    def generate_output(self):
        # return a string of the parachute to be printed
        chute = "  ___  \n /___\\ \n \\   / \n  \\ /\n   0   \n  /|\\   \n  / \\   \n^^^^^^^"
        pass