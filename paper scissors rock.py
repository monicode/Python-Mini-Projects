# --- ROCK - PAPER - SCISSORS --- #

import random

keep_playing = True
count_games = 0
count_wins = 0

print("Let's play!")

while keep_playing:	
	
	count_games +=1
	
	# player choice
	player_choice = input("\nRock[R], Paper[P] or Scissors[S]?").upper()
	if player_choice == "R":
		player_choice = "ROCK"
	elif player_choice == "P":
		player_choice = "PAPER"
	elif player_choice == "S":
		player_choice = "SCISSORS"
	else:
		print ("What is it? You should choose Rock[R], Paper[P] or Scissors[S]. Try again!")
		continue
		
	#computer choice
	computer_choice = random.choice(["ROCK", "PAPER", "SCISSORS"])
	print ("You choice is " + player_choice)
	print ("Computer choice is " + computer_choice)
	
	# comparison player and computer choices
	if player_choice == computer_choice:
		print("Tie!")
	else: 	
		player_win = False
		if player_choice == "ROCK" and computer_choice == "SCISSORS":
			player_win = True
		elif player_choice == "SCISSORS" and computer_choice == "PAPER":
			player_win = True
		elif player_choice == "PAPER" and computer_choice == "ROCK":
			player_win = True
	
		# game result
		if player_win:
			print("You won!")
			count_wins += 1
		else:
			print("Computer won!")
		
	# play or not to play
	while True:
		finish_game = input("\nDo you want to keep playing? Yes or no [Y/N]?").upper()
		if finish_game =="Y":
			keep_playing
		elif finish_game == "N":
			keep_playing = False
			print ("\nNumbers of played games: " + str(count_games))
			print ("Your winning turns: " + str(count_wins))
			print ("Thank you for playing!")
		else:
			print("Please enter Yes[Y] or No[N].")
			continue
		break	
		
# --- end --- #