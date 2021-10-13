from game.parachute import Parachute
from game.console import Console
from game.word import Word

class Director:
    def __init__(self):
        pass
    
    def start_game(self):
        pass

    def get_inputs(self):
        # interacts with console class
        pass

    def do_updates(self):
        # updates game information (word, parachute)
        pass

    def do_outputs(self):
        #handles outputs. Tell console to print out current parachute and word
        pass