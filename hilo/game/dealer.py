from game.card import Card

class Dealer:
    """A person who directs the game. 
    
    The responsibility of a Dealer is to control the sequence of play.

    Attributes:
        current_card([current_card]): An instances of the current card.
        next_card([next_card]): Instance of the card.
        is_playing (boolean): Whether or not the game is being played.
        score (int): score thats start at 300 points.
        total_score (int): The score for the entire game.
    """
    def __init__(self):
        self.current_card = 0
        self.next_card = 0
        self.is_playing = True
        # self.total_score = 0   no need of 2 scores.
        self.score = 300
        self.userGuess = ''

        #instance of the card
        self.current_card = Card()
        self.next_card = Card()

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        while self.is_playing:
            self.get_input()
            self.do_updates()
            self.do_output()

    def get_input(self):
        """Ask the user to guess card.

        Args:
            self (Dealer): An instance of Dealer.
        """

        if (self.current_card.value_card == 0):
            self.current_card.next_card()

        print(f"The card is: {self.current_card.value_card}")
        self.userGuess = input('Higher of lower? [h/l]: ')
        self.next_card.next_card()
        print(f"Next Card was: {self.next_card.value_card}")

    def do_updates(self):
        """Updates the user/player score.

        Args:
            self (Dealer): An instance of Dealer.
        """
        if (self.userGuess.lower() == "h"):
            if(self.current_card.value_card < self.next_card.value_card):
                self.score += 100
            else:
                self.score -=75
        elif(self.userGuess.lower() == "l"):
            if(self.current_card.value_card > self.next_card.value_card):
                self.score += 100
            else:
                self.score -=75
        
        self.current_card.value_card = self.next_card.value_card

        if self.score <= 0:
            self.is_playing = False
            print('Game Over')

    def do_output(self):
        """Display the score and ask the player if he wants to keep playing.
        
        Args:
            self (Dealer): An instance of Dealer.
        """
        if not self.is_playing:
            return
        print(f"Your score is: {self.score}")
        keepPlaying = input("Play again? [y/n]: ")
        if keepPlaying == "y":
            self.is_playing = True
        else:
            self.is_playing = False
            print('Thanks for Playing!! See ya!')


