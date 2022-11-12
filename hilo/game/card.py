import random

class Card:
    """
    
    The responsability is to keep track of the value of the cards
     attributes:
        value_card(int): number of the card
    """
    def __init__(self):
        """Constructs a new instance of card.

        Args:
            self (card): An instance of Card.
        """
        self.value_card = 0
    

    def next_card(self):
        """Generates a new random value for the cards.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value_card = random.randint(1,13)