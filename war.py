from casino import Deck, Player

# logic for the war game

def run_war():
    # game_on continues game logic loop (needs to be better implemented)
    # war_on continues war loop
    # round_num keeps track of game rounds
    game_on, war_on, round_num = True, False, 0

    # player initialization
    player_one, player_two = Player("One"), Player("Two")

    # Create new deck, shuffle 'enough times' to be random
    game_deck = Deck()
    game_deck.shuffle(7)

    # Deal out 26 cards to each player to begin game
    player_one.cards, player_two.cards = game_deck.deal(26), game_deck.deal(26)

    # game_on currently will never be false and instead return statements break the loop.
    # this will be changed in a future update
    while game_on is True:
        # Checks for player lose conditions
        if len(player_one.cards) == 0:
            return 0, 1
        if len(player_two.cards) == 0:
            return 1, 0

        # Increments round number, outputs value
        round_num += 1

        # p1 puts out card, p2 puts out card
        player_one_pile = [player_one.remove_one()]
        player_two_pile = [player_two.remove_one()]

        # if one player's card is greater than the other, they take the pile
        if player_one_pile[0].value > player_two_pile[0].value:
            player_one.add_cards(player_one_pile)
            player_one.add_cards(player_two_pile)
            continue
        elif player_one_pile[0].value < player_two_pile[0].value:
            player_two.add_cards(player_one_pile)
            player_two.add_cards(player_two_pile)
            continue
        else:
            # if both cards are the same value, war is on
            war_on = True

        while war_on and game_on:
            # by design, the first iteration of war will go straight to else
            # statement and come back to compare the top of the piles to
            # see which is larger and determine the winner. if this results
            # in a tie, the war continues
            if player_one_pile[-1].value > player_two_pile[-1].value:
                player_one.add_cards(player_one_pile)
                player_one.add_cards(player_two_pile)
                break
            elif player_one_pile[-1].value < player_two_pile[-1].value:
                player_two.add_cards(player_one_pile)
                player_two.add_cards(player_two_pile)
                break
            else:
                # players will lay down three cards in player order, if
                # either do not have three cards, they will lose.
                if len(player_one.cards) < 3:
                    print(f"P1 win round {round_num}")
                    return 0, 1
                elif len(player_two.cards) < 3:
                    print(f"P2 win round {round_num}")
                    return 1, 0
                else:
                    for i in range(3):
                        player_one_pile.append(player_one.remove_one())
                        player_two_pile.append(player_two.remove_one())
