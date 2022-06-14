from blackjack import run_blackjack
from war import run_war

player_one_wins, player_two_wins = 0, 0

for i in range(10000):
    a, b = run_war()
    player_one_wins += a
    player_two_wins += b

print(f'Player One Wins: {player_one_wins} '
      f'Player Two Wins: {player_two_wins}')

print(f'Player One Win %: {player_one_wins/(player_one_wins+player_two_wins)*100}% '
      f'Player Two Win %: {player_two_wins/(player_one_wins+player_two_wins)*100}%')


player_wins, dealer_wins = 0, 0

for i in range(10000):
    a, b = run_blackjack(14)
    player_wins += a
    dealer_wins += b

print(f'Dealer Wins: {dealer_wins} '
      f'Player Wins: {player_wins}')

print(f'Dealer Win %: {dealer_wins/(player_wins+dealer_wins)*100}% '
      f'Player Win %: {player_wins/(dealer_wins+player_wins)*100}%')
