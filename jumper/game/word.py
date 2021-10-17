import random

class Word:
    """A code template for the secret word. This class chooses the secret word,
    returns the properly redacted printable word.

    Stereotype:
        Information Holder

    Attributes:
        word_list (array): List of words that could be chosen.
        secret_word (string): The word that was chosen from word_list randomly.
        discovered_letters (array): List of letters that have been guessed correctly.
    """
    
    def __init__(self):
        """The class constructor.

        Args:
            self (Word): an instance of Word.
        """
        self.word_list = ["word", "same", "hot", "abstract", "bread", "strange", "miniscule", "absquatulate", "defenestrate", "intense", "unaware"]
        self.secret_word = random.choice(self.word_list)
        self.discovered_letters = []

    def get_word_display(self):
        """Formats the word in a printable and properly redacted way.

        Args:
            self (Word): an instance of Word.
        """
        string = ""
        for x in range(len(self.secret_word)):
            if self.secret_word[x] in self.discovered_letters:
                string += self.secret_word[x]
            else:
                string += "_"
            if x != len(self.secret_word):
                string += " "
        return string

    def check_guess(self, guess):
        """Checks if a guess matches any of the letters in the word.

        Args:
            self (Word): an instance of Word.
            guess (string): the letter being presented as the guess.
        """
        if guess in self.secret_word:
            self.discovered_letters.append(guess)
            return True
        return False

    def word_guessed(self):
        """Checks if the word is completely guessed.

        Args:
            self (Word): an instance of Word.
        """
        for x in range(len(self.secret_word)):
            if self.secret_word[x] not in self.discovered_letters:
                return False
        return True