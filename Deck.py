import random
from Card import Card

class Deck:
    # Default constructor
    def __init__(self):
        self.cards = []
        self.buildDeck()

    def buildDeck(self):
        for value in range(len(Card.value_names)):
            for suit in range(len(Card.suit_names)):
                myCard = Card(value, suit)
                self.cards.append(myCard)
            self.shuffle()

    def draw(self):
        random.choice(self.cards)

    # def pop_card(self):
    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def pop_card(self, i=-1):
        return self.cards.pop(i)

    def deal_top_card(self):
        
    
    def get_first_card(self):

    


