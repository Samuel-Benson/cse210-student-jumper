class Parachute():

    def __init__(self):
        chute = ["  ___  "," /___\\ "," \\   / ","  \\ /","   0   ","  /|\\   ","  / \\   ","^^^^^^^"]
        print(chute[0])
        print(chute[1])
        print(chute[2])
        print(chute[3])
        print(chute[4])
        print(chute[5])
        print(chute[6])
        print(chute[7])
        # Change these print statements into a parachute attribute. (a list)
        return

    def cut(self):
        # makes parachute lose one piece at top
        # SPECIAL CASE: When the last parachute piece is cut, change the stick man's
        # head from a zero ( "   0   " ) to an x ( "   x   " )
        pass

    def is_game_over(self):
        # Return true if the parachute is dead, false it is is not
        pass

    def generate_output(self):
        # return a string of the parachute to be printed
        pass