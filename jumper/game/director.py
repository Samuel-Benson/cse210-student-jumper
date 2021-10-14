from game.parachute import Parachute
from game.console import Console
from game.word import Word

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        gameover (boolean): Whether or not the game can continue.
        parachute (Parachute): An instance of the class of objects known as Parachute.
        word (Word): An instance of the class of objects known as Word.
        letter_guess (Char): The letter input from the console class object. 
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.parachute = Parachute()
        self.console = Console()
        self.word = Word()
        self.gameover = False
        self.letter_guess = ''
    
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while not self.gameover:
            self.do_outputs()
            self.get_inputs()
            self.do_updates()

    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means outputting the current guess state of the word
        and the current state of the parachute.

        Args:
            self (Director): An instance of Director.
        """
        word_output = self.word.get_word_display()
        self.console.write(word_output)
        parachute_output = self.parachute.generate_output()
        self.console.write(parachute_output)


    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means asking the console for a letter guess input.

        Args:
            self (Director): An instance of Director.
        """
        self.letter_guess = self.console.read("Guess a letter [a-z]: ")


    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means the word checks if the user guess is correct or not,
        and the parachute reacts to that result.

        Args:
            self (Director): An instance of Director.
        """
        guessed_correctly = self.word.check_guess(self.letter_guess)
        if not guessed_correctly:
            self.parachute.cut()
            self.gameover = self.parachute.is_game_over()