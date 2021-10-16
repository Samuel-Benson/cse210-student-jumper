class Parachute():

    def __init__(self):
        self.chute = ["  ___  "," /___\\ "," \\   / ","  \\ /","   0   ","  /|\\   ","  / \\   ","^^^^^^^"]
        # Change these print statements into a parachute attribute. (a list)

    def cut(self):
        # makes parachute lose one piece at top
        # SPECIAL CASE: When the last parachute piece is cut, change the stick man's
        # head from a zero ( "   0   " ) to an x ( "   x   " )
        if self.chute.pop(0) == "  \\ /":
            self.chute[0] = "   X   "

    def is_game_over(self):
        # Return true if the parachute is dead, false it is is not
        if self.chute[0] == "   X   ":
            return True
        return False

    def generate_output(self):
        # return a string of the parachute to be printed
        return_string = ""
        for chute_part in self.chute:
            return_string += chute_part + "\n"
        return return_string