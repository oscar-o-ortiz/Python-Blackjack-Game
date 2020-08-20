import random

# create a card object
class Card(object):

    def __init__(self, suit, rank):
        self.suit = str(suit)
        self.rank = str(rank)

    def __str__(self):
        return "[" + self.suit +", " + self.rank + "]"

# create a desk object
class Deck(object):
    suits = ["C", "H", "D", "S"]
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    cards = []

    def __init__(self):
        for suit in self.suits:
            for rank in self.ranks:
                newCard = Card(suit, rank)
                self.cards.append(newCard)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)

# setting up a Blackjack game
#class Game(object):



