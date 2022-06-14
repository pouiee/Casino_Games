import random


# Create dictionary for value assignment upon Card object creation, Aces = 11
value_dict = {'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
              'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}


def make_new_deck():
    # declare suits and cards to iterate through
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    # iterate through the arrays to distribute suits to card values
    # return an ordered array of Card objects
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(Card(suit, rank))
    return deck


class Card:

    def __init__(self, suit, rank):
        # Card object with attribute suit, rank, value
        self.suit = suit
        self.rank = rank
        self.value = value_dict[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    """
    cards = number of decks being created
    A class that allows whatever game to be played
    """

    def __init__(self, cards=None):
        # Creates new, not shuffled deck
        self.cards = make_new_deck()
        if cards is not None:
            for i in range(cards):
                self.cards.extend(make_new_deck())

    def deck_order(self):
        # Outputs cards in order
        for card in self.cards:
            print(card)

    def shuffle(self, num_shuffle=1):
        # Shuffles cards num_shuffle times (1 is sufficient, but more is realistic)
        for i in range(num_shuffle):
            random.shuffle(self.cards)

    def deal(self, cards=1):
        # deals out certain number of cards
        return [self.cards.pop() for i in range(cards)]


class Player:

    def __init__(self, name, chips=None):

        self.name = name
        self.chips = chips
        self.cards = []

    def valuation(self):
        # determine value of hand, using aces as 11s
        total_value = 0
        for card in self.cards:
            total_value += card.value
        return total_value

    def find_aces(self):
        # find amount of aces in player hand
        total_aces = 0
        for card in self.cards:
            if card.rank == 'Ace':
                total_aces += 1
        return total_aces

    def hit(self, pain_threshold, deck):
        while self.valuation() < pain_threshold:
            self.add_cards(deck.deal())
            if self.valuation() > 21:
                if self.find_aces() > 0:
                    return self.valuation()-10
        return self.valuation()

    def remove_one(self):
        return self.cards.pop()

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.cards)} cards.'
