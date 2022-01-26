from Casino import Deck


def blackjack_initialize():
    game_deck = Deck('new')
    game_deck.shuffle(15)
    game_deck.deck_order()
    player_deck, dealer_deck = [], []
    for i in range(2):
        game_deck.deal(player_deck)
        game_deck.deal(dealer_deck)
    game_deck.deck_order()
    player_deck.deck_order()
    dealer_deck.deck_order()
    return game_deck, player_deck, dealer_deck
