from casino import Deck, Card, Player


def run_blackjack(player_pain):
    # Initialize game deck that game is played from, player_pain is the threshold they are
    # willing to take another card
    game_deck = Deck(2)
    game_deck.shuffle(5)

    # Initialize player and dealer Players, player has money to lose
    player, dealer = Player("player", 100), Player("dealer")
    # Numbers used in
    player_wins, dealer_wins = 0, 0
    # keeps game loop going
    game_loop = True

    while game_loop:
        # Starts game loop
        # ends game if player runs out of money
        # else if deck is too small, get two new decks and shuffle
        # else start game, remove 10 chips for player to play
        if player.chips < 10:
            return player_wins, dealer_wins
        elif len(game_deck.cards) < 15:
            game_deck = Deck(2)
            game_deck.shuffle(5)
        else:
            player.chips -= 10

        player.cards, dealer.cards = [], []
        for i in range(2):
            player.add_cards(game_deck.deal())
            dealer.add_cards(game_deck.deal())

        # if dealer has 21, player loses no matter what
        if dealer.valuation() == 21:
            dealer_wins += 1
            continue
        # if player gets less than the dealer
        elif player.hit(player_pain, game_deck) <= dealer.hit(17, game_deck) and not dealer.valuation() > 21:
            dealer_wins += 1
            continue
        elif player.valuation() > 21:
            dealer_wins += 1
            continue
        else:
            player_wins += 1
            player.chips += 10
            continue
