class Card:
    """Represents a standard Bicycle playing card

    Suits: Int 0-3
    Rank: Int 1-13
    # clubs (♣), diamonds (♦), hearts (♥), and spades (♠)
    """
    suit_names = ["♣", "♦", "♥", "♠"]
    value_names = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]


    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    # def __str__(self):
    #     very_special_values = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}


    # String representation
    def __repr__(self):
            return "Card(%s, %s)" % (self.value, self.suit)