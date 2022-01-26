import random
import numpy as np


def make_new_deck():
    # declare suits and cards to iterate through
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    deck = np.empty(52, dtype=Card)
    # iterate through the arrays to distribute suits to card values
    for i in range(13):
        deck[(i-1)*4] = Card(suits[0], cards[i-1])
        deck[(i-1)*4+1] = Card(suits[1], cards[i-1])
        deck[(i-1)*4+2] = Card(suits[2], cards[i-1])
        deck[(i-1)*4+3] = Card(suits[3], cards[i-1])
    # return an ordered array of Card objects
    return deck


def standard_deviation(comparable_deck):
    # method of determining difference between new, unordered deck and comparable deck
    a = make_new_deck()
    return [False if comparable_deck[i] != a[i] else True for i in range(52)]


class Card:

    def __init__(self, suit, card):
        # Card object with attribute suit, card, color, and value
        self.suit = suit
        if self.suit == 'Diamonds' or 'Hearts':
            self.color = 'Red'
        else:
            self.color = 'Black'
        self.card = str(card)
        if card == 'Ace':
            self.value = 1
        elif card == 'Jack' or 'Queen' or 'King':
            self.value = 10
        else:
            self.value = int(card)

    def info(self):
        # Card info display
        print(str(self.card)+ ' of ' + str(self.suit))


class Deck:

    def __init__(self, cards):
        if cards == 'new':
            self.cards = make_new_deck()
        elif cards is None:
            self.cards = []

    def shuffle(self, num_shuffles=1):
        for i in range(52 * num_shuffles):
            card_selector = random.randint(0, 51)
            self.cards.append(self.cards.pop(card_selector))

    def deal(self, other_deck, num_cards=1):
        for i in range(num_cards):
            other_deck.self.cards.np.append(self.cards.pop(-1))

    def deck_order(self):
        for card in self.cards:
            card.info()
