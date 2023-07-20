import random

POSSIBLE_CHOICES = ["r", "p", "s"]

def play_round():
  """Plays a round of rock, paper, scissors."""
  player_1 = input("Player 1, enter your choice (R/P/S): ").lower()
  player_2 = input("Player 2, enter your choice (R/P/S): ").lower()

  if player_1 == player_2:
    return "It's a tie!"

  winning_moves = {"r": "s", "p": "r", "s": "p"}
  if player_1 == winning_moves[player_2.lower()]:
    return "Player 2 won!"
  elif player_2 == winning_moves[player_1.lower()]:
    return "Player 1 won!"
  else:
    return "No winner!"

def main():
  """Plays a round of rock, paper, scissors."""
  result = play_round()
  print(result)

if __name__ == "__main__":
  main()
