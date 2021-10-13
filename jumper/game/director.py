from game.parachute import Parachute
from game.console import Console
from game.word import Word

class Director:
    def __init__(self):
        self.parachute = Parachute()
        self.console = Console()
        self.word = Word()
        self.gameover = False
    
    def start_game(self):
        while not self.gameover:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        # interacts with console class
        letter_guess = self.console.read("Guess a letter [a-z]: ")
        


    def do_updates(self):
        # updates game information (word, parachute)
        pass

    def do_outputs(self):
        #handles outputs. Tell console to print out current parachute and word
        pass