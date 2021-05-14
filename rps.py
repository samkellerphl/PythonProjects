player_one = input("Player one, please insert rock, paper, or scissors: ")
player_two = input("Player two, please insert rock, paper, or scissors: ")

print("Rock, paper, scissors, SHOOT!")

if player_one.upper() == player_two.upper():
	print("It's a draw")
elif player_one.upper() == 'ROCK' and player_two.upper() == 'SCISSORS':
	print("Player one wins")
elif player_one.upper() == 'SCISSORS' and player_two.upper() == 'PAPER':
	print("Player one wins")
elif player_one.upper() == 'PAPER' and player_two.upper() == 'ROCK':
	print("Player one wins")
elif player_two.upper() == 'ROCK' and player_one.upper() == 'SCISSORS':
	print("Player two wins")
elif player_two.upper() == 'SCISSORS' and player_one.upper() == 'PAPER':
	print("Player two wins")
elif player_two.upper() == 'PAPER' and player_one.upper() == 'ROCK':
	print("Player two wins")
else:
	print("Please enter a valid value")